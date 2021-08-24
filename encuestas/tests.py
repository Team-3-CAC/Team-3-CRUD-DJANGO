from django.test import TestCase

# Create your tests here.
class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()

    def testHelloWrold(self): # ejemplo profe
        response = self.client.get("/users/")
        self.assertContains(response , "Hello world from Django for Codo a Codo 4.0")

    def testSatusCodeHelloWorld(self): # ejemplo profe
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200 )


    def testSaludo(self): # Mauricio
        response = self.client.get("/saludo/")
        self.assertContains(response, "Saludos! desde django para codo a codo")
    
    def testWelcome(self): # Paola
        response = self.client.get("/welcome/")
        self.assertContains(response, "Bienvenido desde Django para Codo a Codo 4.0")

    def testDatos(self): # Marcos
        response = self.client.get("/datos/")
        self.assertContains(response, "Por favor complete sus datos personales")

    def testNumero(self): # Fernando
        response = self.client.get("/numero/")
        responseNumber = int(response.content)
        self.assertTrue(responseNumber in range(0,6))


#Testing the CRUD

#    def testRead(self):
#        self.fail()

#    def testUpdate(self):
#        self.fail()

#    def testDelete(self):
#        self.fail()

#    def testCreate(self):
#        self.fail()

'''
def read(request):
    myUsers = User.objects.all()
    print("Hay una cantidad de", len(myUsers), "usuarios registrados actualmente")
    return HttpResponse("READ Hello world from Django for Codo a Codo 4.0:")

def update(data):
    return HttpResponse("UPDATE Hello world from Django for Codo a Codo 4.0:")

def delete(data):
    return HttpResponse("DELETE Hello world from Django for Codo a Codo 4.0:")

def create(data):
    return HttpResponse("CREATE Hello world from Django for Codo a Codo 4.0:")
'''