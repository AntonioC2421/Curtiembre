from django.apps import apps

#Función para pedir todos los datos de algún modelo (ejm: todos los clientes, proveedores, productos)

def get_all_objects(Name_Model):
    #Nombre app, Name_Model es el texto (ej: 'Producto')
    Model_Class = apps.get_model('AplicacionStock', Name_Model)

    all_list = Model_Class.objects.all()
    
    return all_list