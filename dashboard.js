/* ===========================
   DASHBOARD LOGIC
   =========================== */

let bookings = [];
let dashYear = new Date().getFullYear();
let dashMonth = new Date().getMonth();

// Mock Cleaners Data
const cleaners = [
  { id: 1, name: 'Sarah Jenkins', phone: '07700 900123', jobs: 42, rating: '4.9' },
  { id: 2, name: 'Michael O\'Connor', phone: '07700 900456', jobs: 28, rating: '4.8' },
  { id: 3, name: 'Elena Vasile', phone: '07700 900789', jobs: 15, rating: '5.0' }
];

document.addEventListener('DOMContentLoaded', () => {
  loadData();
  setupNav();
  renderOverview();
  renderBookingsTable();
  renderInvoicesTable();
  renderEarningsTable();
  renderCleaners();
  renderDashCalendar();
});

function loadData() {
  const stored = localStorage.getItem('cleaningBookings');
  if (stored) {
    bookings = JSON.parse(stored);
  } else {
    // Demo data if empty
    bookings = [
      {
        ref: 'BK-DEMO-1234',
        service: 'Deep Cleaning',
        date: new Date().toLocaleDateString('en-GB', { weekday:'long',day:'numeric',month:'long',year:'numeric' }),
        time: '10:00 AM',
        customer: 'John Doe',
        email: 'john@example.com',
        phone: '07700 900000',
        address: '10 Downing St, London SW1A 2AA',
        total: 120,
        status: 'Confirmed',
        created: new Date().toISOString(),
        notes: 'Gate code 1234'
      }
    ];
    localStorage.setItem('cleaningBookings', JSON.stringify(bookings));
  }
}

function setupNav() {
  document.querySelectorAll('.sidebar-link[data-view]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      switchView(link.dataset.view);
    });
  });

  // Date in topbar
  const opts = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  document.getElementById('topbarDate').textContent = new Date().toLocaleDateString('en-GB', opts);
}

function switchView(viewId) {
  // Update nav active state
  document.querySelectorAll('.sidebar-link[data-view]').forEach(l => l.classList.remove('active'));
  const activeLink = document.querySelector(`.sidebar-link[data-view="${viewId}"]`);
  if (activeLink) activeLink.classList.add('active');

  // Update title
  const titles = { overview: 'Dashboard', bookings: 'Manage Bookings', calendar: 'Schedule', invoices: 'Invoices', earnings: 'Earnings', cleaners: 'Cleaners Roster', settings: 'Settings' };
  document.getElementById('topbarTitle').textContent = titles[viewId] || 'Dashboard';

  // Show view
  document.querySelectorAll('.dash-view').forEach(v => v.classList.remove('active'));
  document.getElementById(`view-${viewId}`).classList.add('active');

  // Re-render specifics if needed
  if (viewId === 'calendar') renderDashCalendar();
}

// ---- OVERVIEW ----
function renderOverview() {
  const totalRev = bookings.filter(b => b.status !== 'Cancelled').reduce((sum, b) => sum + b.total, 0);
  const pending = bookings.filter(b => b.status === 'Confirmed').length;
  const completed = bookings.filter(b => b.status === 'Completed').length;

  document.getElementById('statRevenue').textContent = `£${totalRev}`;
  document.getElementById('statBookings').textContent = bookings.length;
  document.getElementById('statPending').textContent = pending;
  document.getElementById('statCompleted').textContent = completed;

  document.getElementById('sidebarBookingCount').textContent = pending > 0 ? pending : '';
  document.getElementById('sidebarBookingCount').style.display = pending > 0 ? 'inline-block' : 'none';

  // Recent bookings table
  const tbody = document.getElementById('overviewTableBody');
  const recent = bookings.slice(0, 5);

  if (recent.length === 0) return;

  tbody.innerHTML = '';
  recent.forEach(b => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${b.ref}</strong></td>
      <td>${b.customer}</td>
      <td>${b.service}</td>
      <td>${b.date.split(',')[0]}</td>
      <td>£${b.total}</td>
      <td><span class="status-badge ${b.status.toLowerCase()}">${b.status}</span></td>
      <td><button class="btn btn-ghost btn-sm" onclick="openDispatchModal('${b.ref}')">Manage</button></td>
    `;
    tbody.appendChild(tr);
  });

  // Earnings Summary
  document.getElementById('esRevenue').textContent = `£${totalRev}`;
  document.getElementById('esMonth').textContent = `£${totalRev}`;
  const avg = bookings.length ? (totalRev / bookings.length).toFixed(0) : 0;
  document.getElementById('esAvg').textContent = `£${avg}`;
}

// ---- BOOKINGS & DISPATCH ----
function renderBookingsTable() {
  const tbody = document.getElementById('bookingsTableBody');
  if (bookings.length === 0) return;

  tbody.innerHTML = '';
  bookings.forEach(b => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${b.ref}</strong></td>
      <td>
        <div>${b.customer}</div>
        <div style="font-size:0.75rem;color:var(--grey-600)">${b.phone}</div>
      </td>
      <td>${b.service}</td>
      <td>
        <div>${b.date.split(',')[0]}</div>
        <div style="font-size:0.75rem;color:var(--grey-600)">${b.time}</div>
      </td>
      <td style="max-width:200px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${b.address}</td>
      <td>£${b.total}</td>
      <td><span class="status-badge ${b.status.toLowerCase()}">${b.status}</span></td>
      <td>
        <select class="form-select" style="padding:6px 10px;font-size:0.8rem;width:110px;" onchange="updateStatus('${b.ref}', this.value)">
          <option value="Confirmed" ${b.status==='Confirmed'?'selected':''}>Confirmed</option>
          <option value="Dispatched" ${b.status==='Dispatched'?'selected':''}>Dispatched</option>
          <option value="Completed" ${b.status==='Completed'?'selected':''}>Completed</option>
          <option value="Cancelled" ${b.status==='Cancelled'?'selected':''}>Cancelled</option>
        </select>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function filterBookings() {
  const term = document.getElementById('bookingSearch').value.toLowerCase();
  const stat = document.getElementById('statusFilter').value;
  const rows = document.getElementById('bookingsTableBody').querySelectorAll('tr');

  if (rows.length === 1 && rows[0].classList.contains('empty-row')) return;

  rows.forEach((row, i) => {
    const b = bookings[i];
    if (!b) return;
    const matchSearch = b.customer.toLowerCase().includes(term) || b.ref.toLowerCase().includes(term) || b.service.toLowerCase().includes(term);
    const matchStat = stat === '' || b.status === stat;
    row.style.display = matchSearch && matchStat ? '' : 'none';
  });
}

function updateStatus(ref, newStatus) {
  const idx = bookings.findIndex(b => b.ref === ref);
  if (idx > -1) {
    bookings[idx].status = newStatus;
    localStorage.setItem('cleaningBookings', JSON.stringify(bookings));
    renderOverview();
    renderBookingsTable();
    showToast(`Booking ${ref} marked as ${newStatus}`);
  }
}

function openDispatchModal(ref) {
  const b = bookings.find(x => x.ref === ref);
  if (!b) return;

  const body = document.getElementById('dispatchModalBody');
  let clOpts = cleaners.map(c => `<option value="${c.id}">${c.name} (★ ${c.rating})</option>`).join('');

  body.innerHTML = `
    <div style="margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--grey-100)">
      <div style="font-size:0.85rem;color:var(--grey-600)">Booking Ref</div>
      <div style="font-weight:700;color:var(--navy);font-size:1.1rem;">${b.ref}</div>
    </div>
    <div style="margin-bottom:20px;">
      <div style="font-size:0.85rem;color:var(--grey-600);margin-bottom:4px;">Service Details</div>
      <div><strong>${b.service}</strong></div>
      <div>${b.date} at ${b.time}</div>
      <div style="margin-top:8px;"><strong>Address:</strong> ${b.address}</div>
      ${b.notes ? `<div style="margin-top:8px;padding:8px;background:var(--off-white);border-radius:4px;font-size:0.85rem;"><em>Note: ${b.notes}</em></div>` : ''}
    </div>
    <div class="form-group" style="margin-bottom:24px;">
      <label class="form-label">Assign Cleaner</label>
      <select class="form-select" id="dispatchCleaner">
        <option value="">Select a cleaner...</option>
        ${clOpts}
      </select>
    </div>
    <button class="btn btn-primary" style="width:100%;justify-content:center;" onclick="dispatchJob('${b.ref}')">Dispatch & Notify Cleaner</button>
  `;
  document.getElementById('dispatchModal').style.display = 'flex';
}

function dispatchJob(ref) {
  const clSel = document.getElementById('dispatchCleaner');
  if (!clSel.value) {
    showToast('Please select a cleaner.', 'error');
    return;
  }
  updateStatus(ref, 'Dispatched');
  document.getElementById('dispatchModal').style.display = 'none';
  showToast('Job dispatched successfully! SMS sent to cleaner.');
}

function closeModal(e) {
  if (e.target.id === 'dispatchModal') {
    e.target.style.display = 'none';
  }
}

// ---- INVOICES & EARNINGS ----
function renderInvoicesTable() {
  const tbody = document.getElementById('invoicesTableBody');
  if (bookings.length === 0) return;
  tbody.innerHTML = '';
  bookings.forEach(b => {
    const invNum = 'INV-' + b.ref.split('-')[1];
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${invNum}</strong></td>
      <td>${b.customer}</td>
      <td>${new Date(b.created).toLocaleDateString('en-GB')}</td>
      <td>Due on Receipt</td>
      <td>£${b.total}</td>
      <td><span class="status-badge completed">Paid</span></td>
      <td>
        <button class="btn btn-ghost btn-sm" onclick="viewInvoice('${b.ref}')">View PDF</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function viewInvoice(ref) {
  // Store ref in session storage to load in invoice.html
  sessionStorage.setItem('currentInvoiceRef', ref);
  window.open('invoice.html', '_blank');
}

function renderEarningsTable() {
  const tbody = document.getElementById('earningsTableBody');
  if (bookings.length === 0) return;
  tbody.innerHTML = '';
  bookings.filter(b => b.status !== 'Cancelled').forEach(b => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${b.ref}</td>
      <td>${b.customer}</td>
      <td>${b.service}</td>
      <td>${b.date.split(',')[0]}</td>
      <td class="text-gold" style="font-weight:700;">+£${b.total}</td>
      <td><span class="status-badge completed">Settled</span></td>
    `;
    tbody.appendChild(tr);
  });
}

// ---- CLEANERS ----
function renderCleaners() {
  const grid = document.getElementById('cleanersGrid');
  grid.innerHTML = '';
  cleaners.forEach(c => {
    grid.innerHTML += `
      <div class="cleaner-card">
        <div class="cl-avatar">${c.name.charAt(0)}</div>
        <div class="cl-name">${c.name}</div>
        <div class="cl-phone">📞 ${c.phone}</div>
        <div class="cl-stats">
          <div class="cl-stat-item"><span class="cls-val">${c.jobs}</span><span class="cls-lbl">Jobs</span></div>
          <div class="cl-stat-item"><span class="cls-val">★ ${c.rating}</span><span class="cls-lbl">Rating</span></div>
        </div>
      </div>
    `;
  });
}

function addCleaner() {
  showToast('Cleaner management portal coming soon.', 'info');
}

// ---- CALENDAR ----
function renderDashCalendar() {
  const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  document.getElementById('dashCalLabel').textContent = `${months[dashMonth]} ${dashYear}`;

  const grid = document.getElementById('dashCalGrid');
  grid.innerHTML = '';

  const firstDay = new Date(dashYear, dashMonth, 1);
  let startDow = firstDay.getDay(); // 0=Sun
  startDow = startDow === 0 ? 6 : startDow - 1; // Mon-based

  const daysInMonth = new Date(dashYear, dashMonth + 1, 0).getDate();

  for (let i = 0; i < startDow; i++) {
    grid.innerHTML += `<div class="dc-cell empty" style="background:transparent;border:none;"></div>`;
  }

  for (let d = 1; d <= daysInMonth; d++) {
    // Find bookings for this day
    const dayStr = `${d} ${months[dashMonth]} ${dashYear}`;
    const dayBookings = bookings.filter(b => b.date.includes(dayStr));

    let jobsHtml = '';
    dayBookings.forEach(b => {
      jobsHtml += `<div class="dc-job" onclick="openDispatchModal('${b.ref}')">${b.time} - ${b.service.split(' ')[0]}</div>`;
    });

    grid.innerHTML += `
      <div class="dc-cell">
        <div class="dc-date">${d}</div>
        ${jobsHtml}
      </div>
    `;
  }
}

function dashCalPrev() {
  if (dashMonth === 0) { dashMonth = 11; dashYear--; }
  else dashMonth--;
  renderDashCalendar();
}

function dashCalNext() {
  if (dashMonth === 11) { dashMonth = 0; dashYear++; }
  else dashMonth++;
  renderDashCalendar();
}
