document.getElementById('process-btn').addEventListener('click', async () => {
  const fileInput = document.getElementById('pdf-upload');
  
  // Check if a file is selected
  if (fileInput.files.length === 0) {
    alert('Please select a PDF file to upload.');
    return;
  }
  
  // Get the file and append it to a FormData object
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('pdf', file);
  
  try {
    // Send a POST request to your Render URL endpoint
    const response = await fetch('https://pdf-note-generator.onrender.com/upload', {
      method: 'POST',
      body: formData
    });
    
    // Check for any network errors
    if (!response.ok) {
      throw new Error(`Server error: ${response.statusText}`);
    }
    
    // Get the JSON response from your backend
    const result = await response.json();
    
    // Display the extracted notes in the "notes" div
    document.getElementById('notes').innerHTML = `<pre>${result.notes}</pre>`;
    
  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred while processing the PDF.');
  }
});
