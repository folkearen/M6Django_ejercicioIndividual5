from django import forms
from ..models import *
#Etiqueta meta
#model: Este atributo se usa cuando se desea crear un formulario basado en un modelo (ModelForm). Indica el modelo en el que se basará el formulario, y Django generará automáticamente los campos del formulario según los campos del modelo.
# fields: Se utiliza en los ModelForms para indicar qué campos del modelo se incluirán en el formulario. Puedes especificar una lista de nombres de campos que deseas mostrar en el formulario.
# exclude: Otra opción para ModelForms, donde se puede especificar una lista de campos que no se incluirán en el formulario.
# widgets: Te permite definir widgets personalizados para los campos del formulario. Los widgets controlan cómo se renderizan los campos en el frontend.
# labels: Puedes proporcionar etiquetas personalizadas para los campos del formulario mediante un diccionario donde las claves son los nombres de los campos y los valores son las etiquetas deseadas.
# help_texts: Similar a labels, te permite proporcionar texto de ayuda personalizado para los campos mediante un diccionario.
# error_messages: Permite personalizar los mensajes de error para campos específicos en caso de que la validación falle.

class signUp(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=254, required=True)
    password = forms.CharField(max_length=12, required=True)
    confirm_password = forms.CharField(max_length=12, required=True)
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password']
