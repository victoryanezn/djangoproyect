from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('contacto/', views.contacto, name= "contacto"),
    path('reglas/', views.reglas, name= "reglas"),
    path('tienda/', views.tienda, name= "tienda"),
    path('agregar-producto/', views.agregar_producto, name="agregar_producto"),
    path('listar-productos/', views.listar_productos, name="listar_productos"),
    path('modificar-productos/<id>/', views.modificar_producto, name="modificar_productos"),
    path('eliminar-producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('registro/', views.registro, name ="registro"),
    path('feedbacks/', views.feedbacks, name ="feedbacks"),

    # --
    path('agregar-feedback/', views.agregar_feedback, name="agregar_feedback"),
    path('listar-feedbacks/', views.listar_feedbacks, name="listar_feedbacks"),
    path('modificar-feedbacks/<id>/', views.modificar_feedback, name="modificar_feedbacks"),
    path('eliminar-feedback/<id>/', views.eliminar_feedback, name="eliminar_feedback"),
    

]

# ----------------------------------
#             Chuly
#     GitHub: https://github.com/victoryanezn
#     Discord: chuly2005#0
# ---------------------------------- 