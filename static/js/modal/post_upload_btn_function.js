function openFile() {
  document.getElementById('imageInput').click();
}

document.getElementById('imageInput').addEventListener('change', function(event) {
  const file = event.target.files[0];
  if (file) {
    // Set the file name display
    document.getElementById('fileNameDisplay').innerText = `Selected file: ${file.name}`;

    // Show preview in second modal
    const reader = new FileReader();
    reader.onload = function(e) {
      const preview = document.getElementById('imagePreview');
      preview.src = e.target.result;
      preview.classList.remove('d-none');
    };
    reader.readAsDataURL(file);

    // Sync file to hidden input in second modal
    const dt = new DataTransfer();
    dt.items.add(file);
    document.getElementById('postImageInput').files = dt.files;
  }
});

function openSecondModal() {
  const firstModal = bootstrap.Modal.getInstance(document.getElementById('createPostModal'));
  firstModal.hide();

  const secondModalEl = document.getElementById('secondModal');
  const secondModal = new bootstrap.Modal(secondModalEl);
  secondModal.show();
}
