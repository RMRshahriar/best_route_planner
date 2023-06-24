const form = document.getElementById('routeForm');
form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form submission from refreshing the page

  const startLocation = form.elements.start.value;
  const endLocation = form.elements.end.value;
  const selectedDate = form.elements.date.value;
  const selectedMonth = form.elements.month.value;
  const selectedTime = form.elements.time.value;

  // Perform actions based on the selected values
  // e.g., display route on the map

  // Clear form inputs (optional)
  form.reset();
});