function previewImage(event) {
    const file = event.target.files[0];

    const reader = new FileReader();
    reader.onload = function () {
        const output = document.getElementById('profileImage');
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(file);

    const formData = new FormData();
    formData.append('image', file);
    formData.append('csrfmiddlewaretoken', csrfToken);

    fetch(uploadUrl, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) throw new Error('Upload failed');
        return response.json();
    })
    .then(data => {
        document.getElementById('profileImage').src = data.url;
        
    })
    .catch(error => {
        console.error('Upload error:', error);
        alert('Image upload failed!');
    });
}

