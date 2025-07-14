document.addEventListener('DOMContentLoaded', function () {
  const createBtn = document.getElementById('createBtn');
  const createOptions = document.getElementById('createOptions');
  const openPostModal = document.getElementById('openPostModal');

  if (createBtn && createOptions) {
    // Toggle on button click
    createBtn.addEventListener('click', (event) => {
      event.stopPropagation(); // Prevent triggering the document click
      if (createOptions.style.display === 'flex') {
        createOptions.style.display = 'none';
      } else {
        createOptions.style.display = 'flex';
      }
    });

    // Prevent click inside options from closing it
    createOptions.addEventListener('click', (event) => {
      event.stopPropagation();
    });

    // Hide on click outside
    document.addEventListener('click', () => {
      createOptions.style.display = 'none';
    });
  }

  // Modal trigger
  if (openPostModal) {
    openPostModal.addEventListener('click', () => {
      const myModal = new bootstrap.Modal(document.getElementById('createPostModal'));
      myModal.show();
    });
  }
});
