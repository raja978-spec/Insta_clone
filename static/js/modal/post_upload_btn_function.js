// Function to open the hidden file input
function openFile() {
  document.getElementById('imageInput').click();
}

// Image preview logic
document.getElementById('imageInput').addEventListener('change', function(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      const preview = document.getElementById('imagePreview');
      preview.src = e.target.result;
      preview.classList.remove('d-none');
    };
    reader.readAsDataURL(file);

    // Show selected filename
    document.getElementById('fileNameDisplay').innerText = `Selected file: ${file.name}`;
  }
});

 function openSecondModal() {
    const firstModal = bootstrap.Modal.getInstance(document.getElementById('createPostModal'));
    firstModal.hide();
    

    const secondModalEl = document.getElementById('secondModal');
    const secondModal = new bootstrap.Modal(secondModalEl);
    secondModal.show();
  }
