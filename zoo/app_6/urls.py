from django.urls import path
from .views import view_habitat, view_animal

urlpatterns = [
    path('', view_habitat.home_view, name='view00' ),
    path('habitatINsert', view_habitat.insert_habitat_view , name='view01'),
    path('habitatLIst', view_habitat.list_habitat_view , name='view02'),
    path('habitatDelete/<int:id>', view_habitat.delete_habitat_view , name='view03'),
    path('habitatUpdate/<int:id>', view_habitat.update_habitat_view , name='view04'),
    path('animalINsert', view_animal.insert_animal_view , name='view001'),
    path('animalLIst', view_animal.list_animal_view , name='view002'),
    path('animalDelete/<int:id>', view_animal.delete_animal_view , name='view003'),
    path('animalUpdate/<int:id>', view_animal.update_animal_view , name='view004'),
]