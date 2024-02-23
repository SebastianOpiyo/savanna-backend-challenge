from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer

class CustomerListCreateAPIViewTestCase(APITestCase):
    url = reverse('customer-list-create')  # Assuming 'customer-list-create' is the URL name for CustomerListCreateAPIView

    def test_create_customer(self):
        data = {'name': 'Test Customer', 'email': 'test@example.com'}  # Sample data for creating a customer
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Test Customer')

    def test_list_customers(self):
        Customer.objects.create(name='Customer 1', email='customer1@example.com')
        Customer.objects.create(name='Customer 2', email='customer2@example.com')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Customer 1')
        self.assertEqual(response.data[1]['name'], 'Customer 2')

class CustomerRetrieveUpdateDestroyAPIViewTestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer', email='test@example.com')
        self.url = reverse('customer-detail', kwargs={'pk': self.customer.pk})  # Assuming 'customer-detail' is the URL name for CustomerRetrieveUpdateDestroyAPIView

    def test_retrieve_customer(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Customer')

    def test_update_customer(self):
        data = {'name': 'Updated Customer', 'email': 'updated@example.com'}
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get(pk=self.customer.pk).name, 'Updated Customer')

    def test_delete_customer(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)

