from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Food

class ListView(View):
    def get(self, request):
        foods = Food.objects.all()
        return render(request, 'index.html', {'foods': foods})

class DetailView(View):
    def get(self, request, pk):
        food = get_object_or_404(Food, id=pk)
        return render(request, 'detail_food.html', {'food': food})

class CreateView(View):
    def get(self, request):
        return render(request, 'create_food.html')

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        composition = request.POST.get('composition')
        preparation_time = request.POST.get('preparation_time')
        created_at = request.POST.get('created_at')

        Food.objects.create(
            title=title,
            price=price,
            composition=composition,
            preparation_time=preparation_time,
            created_at=created_at
        )
        return redirect('index')

class UpdateView(View):
    def get(self, request, pk):
        food = get_object_or_404(Food, id=pk)
        return render(request, 'update_food.html', {'food': food})

    def post(self, request, pk):
        food = get_object_or_404(Food, id=pk)
        food.title = request.POST['title']
        food.price = request.POST['price']
        food.composition = request.POST['composition']
        food.preparation_time = request.POST['preparation_time']
        food.created_at = request.POST['created_at']
        food.save()
        return redirect('index')

class DeleteView(View):
    def post(self, request, pk):
        food = get_object_or_404(Food, id=pk)
        food.delete()
        return redirect('index')
