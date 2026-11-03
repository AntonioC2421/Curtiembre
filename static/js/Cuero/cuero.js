function actualizarColor(valor) {
    var preview = document.getElementById('colorPreview');
    if (!preview) return;

    valor = valor.trim();

    // 1. Formato RGB tipo 255.0.0 o 255,0,0
    if (/^\d{1,3}[\.,\s]+\d{1,3}[\.,\s]+\d{1,3}$/.test(valor)) {
        var partes = valor.split(/[\.,\s]+/);
        preview.style.backgroundColor = 'rgb(' + partes[0] + ',' + partes[1] + ',' + partes[2] + ')';
        return;
    }

    // 2. Si es Hexadecimal de 6 dígitos sin # (ej: FF5733)
    if (/^[0-9A-Fa-f]{6}$/.test(valor)) {
        valor = '#' + valor;
    }

    // 3. Si es Hexadecimal válido con #
    if (/^#[0-9A-Fa-f]{6}$/.test(valor)) {
        preview.style.backgroundColor = valor;
    }
}