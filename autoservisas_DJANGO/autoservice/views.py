from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,  get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from .forms import OrderCreateForm, OrderLineCreateForm
from .models import Car_model, Car, Order, Service, Order_line, CarReview
from django.views import generic, View
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import CarReviewForm, UserUpdateForm, ProfilisUpdateForm, OrderCreateForm, CombinedOrderForm, OrderUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import OrderUpdateForm
from django.views.generic import UpdateView
from django.views.generic.edit import FormMixin, DeleteView


# Create your views here.
def index(request):
    #suskaiciuojame kiek yra paslaugu
    num_services_2as = Service.objects.all().count()

    # suskaiciuojame kiek yra pabaigtu darbu pagal filtra == p
    num_services_done = Order.objects.filter(status='p').count()

    num_car = Car.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_services_2': num_services_2as,
        'num_services_done': num_services_done,
        'num_car': num_car,
        'num_visits': num_visits
        # Įtrauk kitus duomenis, kuriuos nori rodyti šiame puslapyje
    }

    return render(request, 'index.html', context)

def cars(request):
    paginator = Paginator(Car.objects.all(), 2)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
    context = {
        'cars': cars
    }
    print(cars)
    return render(request, 'cars.html', context=context)

@csrf_protect
def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        form = CarReviewForm(request.POST)
        if form.is_valid():
            form.instance.car = single_car
            form.instance.reviewer = request.user
            form.save()

    form = CarReviewForm()
    car_reviews = single_car.carreview_set.all()

    context = {
        'license_plate': single_car.license_plate,
        'car_model': single_car.car_model,
        'vin_code': single_car.vin_code,
        'client': single_car.client,
        'car_reviews': car_reviews,
        'form': form
    }

    return render(request, 'car_detail.html', context=context)


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 2
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        # gaunamas car_id ir status naudojant GET request
        car_id = self.request.GET.get('car_id')
        status = self.request.GET.get('status')

        # Uzklausa kuriuos parametrus paimti
        queryset = Order.objects.all()

        if car_id:
            queryset = queryset.filter(car__id=car_id)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

def search(request):
    """
        paprasta paieška. query ima informaciją iš paieškos laukelio,
        search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
        Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
        didžiosios/mažosios.
        """
    query = request.GET.get('query')
    search_results = Car.objects.filter(
        Q(client__icontains=query) |  # Assuming 'name' is a field in the related model
        Q(car_model__make__icontains=query) |
        Q(car_model__model__icontains=query) |
        Q(license_plate__icontains=query) |
        Q(vin_code__icontains=query)
    )
    return render(request, 'search.html', {'cars': search_results, 'query': query})


class OngoingWorkByUserListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'user_orders.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(reader=self.request.user, status='v').order_by('data')


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos !!
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai !!
        if password == password2:
            # tikriname, ar neužimtas username !!
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email !!
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją !!
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

class CarDetailView(FormMixin, generic.DetailView):
    model = Car
    template_name = 'car_detail.html'
    form_class = CarReviewForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('car-detail', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *arg, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.car = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(CarDetailView, self).form_valid(form)


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html', context)

class OrdersByUserListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'user_orders'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(read=self.request.user).order_by('due_back')

class OrdersByUserDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'user_orders.html'

class OrdersByUserCreateView(LoginRequiredMixin, CreateView):
    form_class = CombinedOrderForm
    success_url = reverse_lazy('order-list')
    template_name = "order_form.html"

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

class OrdersByUsersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order  # Replace this with the actual import path for your Order model
    form_class = OrderUpdateForm
    template_name = "order_form.html"
    success_url = reverse_lazy('order-list')

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.reader

class OrderByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')
    template_name = 'user_order_delete.html'

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.reader