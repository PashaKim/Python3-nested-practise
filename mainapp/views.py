from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet



from rest_framework import generics, permissions
from .models import Groups, Elements
from .serializers import GroupsSerializer, ElementsSerializer


class GroupsListView(ModelViewSet):
    serializer_class = GroupsSerializer
    queryset = Groups.objects.all()
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )


class GroupsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupsSerializer
    queryset = Groups.objects.all()
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ElementsListView(ModelViewSet):
    serializer_class = ElementsSerializer
    queryset = Elements.objects.filter(moderated=True).all()


class ElementsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ElementsSerializer
    queryset = Elements.objects.filter(moderated=True).all()

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('elements')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
