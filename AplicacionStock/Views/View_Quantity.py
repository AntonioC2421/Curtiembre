from django.apps import apps

#Función para pedir una cantidad especifica de algún modelo (ejm: 12 clientes, 10 productos)
def get_quantity_objects(Name_Model, Quantity):
    Model_Class = apps.get_model('AplicacionStock', Name_Model)

    Quantity_Register = Model_Class.objects.order_by('-id')[:Quantity]

    return Quantity_Register

