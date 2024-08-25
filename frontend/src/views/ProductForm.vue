<template>
  <div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="name">Product Name:</label>
        <input v-model="formData.name" id="name" type="text" required />
      </div>
      <div>
        <label for="price">Price:</label>
        <input v-model="formData.price" id="price" type="number" required />
      </div>
      <div>
        <label for="category">Category:</label>
        <input v-model="formData.category.title" id="category" type="text" required />
      </div>
      <div>
        <label for="evaluation">Evaluation:</label>
        <input v-model="formData.evaluation" id="evaluation" type="number" required />
      </div>
      <button type="submit">Submit</button>
      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const formData = ref({
  name: '',
  price: '',
  category: {
    title: ''
  },
  evaluation: 0
});

const errorMessage = ref('');

function validateForm() {
  if (formData.value.price <= 0) {
    errorMessage.value = 'Price must be greater than 0.';
    return false;
  }

  if (!formData.value.name || !formData.value.category.title) {
    errorMessage.value = 'Name and Category are required.';
    return false;
  }

  errorMessage.value = '';
  return true;
}

async function submitForm() {
  if (!validateForm()) {
    return;
  }

  try {
    const response = await fetch('http://127.0.0.1:8000/api/products/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Add other headers if needed (e.g., authentication tokens)
      },
      body: JSON.stringify(formData.value)
    });

    if (!response.ok) {
      throw new Error('Network response was not ok.');
    }

    const result = await response.json();
    console.log('Success:', result);
  } catch (error) {
    console.error('Error:', error);
  }
}
</script>
