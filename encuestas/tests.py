from django.test import TestCase

# Create your tests here.


class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()

    def testHelloWrold(self):
        request = self.client.get("/users/")
        self.assertEqual(request.content, "Hello world from Django for Codo a Codo 4.0")

    def testSegundoHelloWorld(self):
        self.fail()

    def testSaludo(self):
        request = self.client.get("/saludo/")
        self.assertEqual(request.content, "Saludos! desde django para codo a codo")
    
    def testWelcome(self):
        request = self.client.get("/welcome/")
        self.assertEqual(request.content , "Bienvenido desde Django para Codo a Codo 4.0")

    def testDatos(self):
        request = self.client.get("/datos/")
        self.assertEqual(request.content, "Por favor complete sus datos personales")