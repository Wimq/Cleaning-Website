/* ===========================
   INVOICE LOGIC
   =========================== */

document.addEventListener('DOMContentLoaded', () => {
  const ref = sessionStorage.getItem('currentInvoiceRef');
  if (!ref) {
    // Demo mode if accessed directly without a booking
    document.title = 'Invoice - Demo';
    return;
  }

  const stored = localStorage.getItem('cleaningBookings');
  if (!stored) return;

  const bookings = JSON.parse(stored);
  const b = bookings.find(x => x.ref === ref);
  if (!b) return;

  // Update DOM elements
  document.title = `Invoice ${ref} - [Business Name]`;

  document.getElementById('invCustomerName').textContent = b.customer;
  document.getElementById('invCustomerAddr').innerHTML = b.address.replace(/, /g, '<br/>');
  document.getElementById('invCustomerEmail').textContent = b.email;
  document.getElementById('invCustomerPhone').textContent = b.phone || '';

  document.getElementById('invNumber').textContent = 'INV-' + b.ref.split('-')[1];
  
  // Try to parse the created date, fallback to current if invalid
  let createdDate = new Date(b.created);
  if (isNaN(createdDate.getTime())) createdDate = new Date();
  
  document.getElementById('invDate').textContent = createdDate.toLocaleDateString('en-GB', { day:'2-digit', month:'short', year:'numeric' });
  document.getElementById('invRef').textContent = b.ref;

  // Items
  const itemsHtml = `
    <tr>
      <td>
        <div style="font-weight:600;">${b.service}</div>
        <div style="font-size:0.85em;color:var(--grey-600);">Service provided on ${b.date} at ${b.time}</div>
      </td>
      <td>1</td>
      <td style="text-align:right;">£${b.total.toFixed(2)}</td>
    </tr>
  `;
  document.getElementById('invItems').innerHTML = itemsHtml;

  // Totals
  document.getElementById('invSubtotal').textContent = `£${b.total.toFixed(2)}`;
  document.getElementById('invTotal').textContent = `£${b.total.toFixed(2)}`;
});
