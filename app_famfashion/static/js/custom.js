// FAMFASHION - Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Table row selection
    const tableRows = document.querySelectorAll('.table tbody tr[data-href]');
    tableRows.forEach(row => {
        row.style.cursor = 'pointer';
        row.addEventListener('click', function() {
            window.location.href = this.dataset.href;
        });
    });

    // Image preview for file inputs
    const imageInputs = document.querySelectorAll('input[type="file"][accept^="image"]');
    imageInputs.forEach(input => {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    // Create or update preview
                    let preview = input.parentNode.querySelector('.image-preview');
                    if (!preview) {
                        preview = document.createElement('div');
                        preview.className = 'image-preview mt-2';
                        input.parentNode.appendChild(preview);
                    }
                    preview.innerHTML = `<img src="${e.target.result}" class="img-thumbnail" style="max-width: 200px; max-height: 200px;">`;
                };
                reader.readAsDataURL(file);
            }
        });
    });

    // Auto-calculate totals for order forms
    const quantityInputs = document.querySelectorAll('input[name="cantidad"]');
    const priceInputs = document.querySelectorAll('input[name="precio_unitario"]');
    const totalInputs = document.querySelectorAll('input[name="total"]');

    function calculateTotal() {
        const quantity = parseFloat(this.closest('.row').querySelector('input[name="cantidad"]').value) || 0;
        const price = parseFloat(this.closest('.row').querySelector('input[name="precio_unitario"]').value) || 0;
        const total = quantity * price;
        
        const totalInput = this.closest('.row').querySelector('input[name="total"]');
        if (totalInput) {
            totalInput.value = total.toFixed(2);
        }
    }

    quantityInputs.forEach(input => input.addEventListener('input', calculateTotal));
    priceInputs.forEach(input => input.addEventListener('input', calculateTotal));

    // Search functionality for tables
    const searchInputs = document.querySelectorAll('.table-search');
    searchInputs.forEach(input => {
        input.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const table = this.closest('.card').querySelector('table');
            const rows = table.querySelectorAll('tbody tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    });

    // Confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete-confirm');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que deseas eliminar este elemento? Esta acción no se puede deshacer.')) {
                e.preventDefault();
            }
        });
    });

    // Real-time stock validation
    const stockInputs = document.querySelectorAll('input[name="stock"]');
    stockInputs.forEach(input => {
        input.addEventListener('blur', function() {
            const value = parseInt(this.value);
            if (value < 0) {
                this.value = 0;
                this.classList.add('is-invalid');
            } else {
                this.classList.remove('is-invalid');
            }
        });
    });

    // Price formatting
    const priceInputsAll = document.querySelectorAll('input[name="precio"], input[name="precio_unitario"]');
    priceInputsAll.forEach(input => {
        input.addEventListener('blur', function() {
            const value = parseFloat(this.value);
            if (!isNaN(value)) {
                this.value = value.toFixed(2);
            }
        });
    });

    // Dynamic date display
    function updateDateTime() {
        const now = new Date();
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        };
        const dateTimeString = now.toLocaleDateString('es-MX', options);
        
        const dateElements = document.querySelectorAll('.current-datetime');
        dateElements.forEach