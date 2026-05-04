/* ===========================
   BOOKING LOGIC
   =========================== */

// State
const state = {
  currentStep: 1,
  service: null,
  serviceLabel: '',
  basePrice: 0,
  extrasPrice: 0,
  bedroomAdjust: 0,
  bedrooms: '2',
  bathrooms: '1',
  frequency: 'One-off',
  postcode: '',
  selectedDate: null,
  selectedTime: null,
  calYear: null,
  calMonth: null,
};

// Adjustments
const BEDROOM_ADJUST = { '0': -20, '1': -10, '2': 0, '3': 20, '4': 40, '5': 60 };

const ALL_TIMES = [
  { t: '8:00 AM', avail: true }, { t: '9:00 AM', avail: true },
  { t: '10:00 AM', avail: false }, { t: '11:00 AM', avail: true },
  { t: '12:00 PM', avail: true }, { t: '1:00 PM', avail: false },
  { t: '2:00 PM', avail: true }, { t: '3:00 PM', avail: true },
  { t: '4:00 PM', avail: true }, { t: '5:00 PM', avail: false },
];

function goStep(n) {
  if (n === 2 && !state.service) { showToast('Please select a service first.', 'error'); return; }
  if (n === 3 && (!state.selectedDate || !state.selectedTime)) { showToast('Please select a date and time.', 'error'); return; }
  if (n === 4) {
    const terms = document.getElementById('termsAgree');
    if (terms && !terms.checked) { showToast('Please agree to the Terms to continue.', 'error'); return; }
  }

  document.querySelectorAll('.booking-step').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.bpb-step').forEach(s => s.classList.remove('active', 'completed'));
  document.querySelectorAll('.bpb-line').forEach(l => l.classList.remove('completed'));

  for (let i = 1; i < n; i++) {
    document.getElementById(`prog-${i}`).classList.add('completed');
    const line = document.getElementById(`line-${i}`);
    if (line) line.classList.add('completed');
  }

  document.getElementById(`step-${n}`).classList.add('active');
  document.getElementById(`prog-${n}`).classList.add('active');
  state.currentStep = n;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function selectService(el, svc, label, price) {
  document.querySelectorAll('.service-sel-card').forEach(c => c.classList.remove('selected'));
  el.classList.add('selected');
  state.service = svc;
  state.serviceLabel = label;
  state.basePrice = price;
  updateQuote();
}

function updateQuote() {
  state.bedrooms = document.getElementById('bedrooms')?.value || '2';
  state.bathrooms = document.getElementById('bathrooms')?.value || '1';
  state.frequency = document.getElementById('frequency')?.value || 'One-off';
  state.postcode = document.getElementById('postcode')?.value || '';

  state.bedroomAdjust = BEDROOM_ADJUST[state.bedrooms] || 0;

  let extras = 0;
  document.querySelectorAll('.extra-check:checked').forEach(cb => {
    extras += parseInt(cb.dataset.price || 0);
  });
  state.extrasPrice = extras;

  if (!state.service) return;

  const total = state.basePrice + state.bedroomAdjust + state.extrasPrice;

  document.getElementById('osBreakdown').style.display = 'block';
  document.getElementById('osBase').textContent = `£${state.basePrice}`;
  
  const extrasLine = document.getElementById('osExtrasLine');
  if (extras > 0) { extrasLine.style.display = 'flex'; document.getElementById('osExtras').textContent = `+£${extras}`; }
  else extrasLine.style.display = 'none';

  const bedroomsLine = document.getElementById('osBedroomsLine');
  if (state.bedroomAdjust !== 0) {
    bedroomsLine.style.display = 'flex';
    document.getElementById('osBedrooms').textContent = (state.bedroomAdjust > 0 ? '+' : '') + `£${state.bedroomAdjust}`;
  } else bedroomsLine.style.display = 'none';

  document.getElementById('osTotal').textContent = `£${Math.max(total, 0)}`;

  document.getElementById('osServiceBlock').innerHTML = `
    <div>
      <div class="os-service-name">${state.serviceLabel}</div>
      <div class="os-service-details">
        ${state.bedrooms === '0' ? 'Studio' : state.bedrooms + ' Bed'} · ${state.bathrooms} Bath<br/>
        ${state.frequency}${state.postcode ? ' · ' + state.postcode.toUpperCase() : ''}
      </div>
    </div>`;

  updateOsDetails();
}

function initCalendar() {
  const now = new Date();
  state.calYear = now.getFullYear();
  state.calMonth = now.getMonth();
  renderCalendar();
}

function renderCalendar() {
  const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  document.getElementById('calMonthLabel').textContent = `${months[state.calMonth]} ${state.calYear}`;

  const grid = document.getElementById('calendarGrid');
  grid.innerHTML = '';
  const today = new Date(); today.setHours(0,0,0,0);
  const firstDay = new Date(state.calYear, state.calMonth, 1);
  let startDow = firstDay.getDay() === 0 ? 6 : firstDay.getDay() - 1;
  const daysInMonth = new Date(state.calYear, state.calMonth + 1, 0).getDate();

  for (let i = 0; i < startDow; i++) grid.innerHTML += `<div class="cal-day empty"></div>`;

  for (let d = 1; d <= daysInMonth; d++) {
    const dayDate = new Date(state.calYear, state.calMonth, d);
    const isPast = dayDate < today;
    const isToday = dayDate.getTime() === today.getTime();
    const isSelected = state.selectedDate && state.selectedDate.getTime() === dayDate.getTime();

    const el = document.createElement('div');
    el.className = 'cal-day' + (isPast ? ' disabled' : '') + (isToday ? ' today' : '') + (isSelected ? ' selected' : '');
    el.textContent = d;
    if (!isPast) el.addEventListener('click', () => selectDate(dayDate, el));
    grid.appendChild(el);
  }
}

function selectDate(date, el) {
  document.querySelectorAll('.cal-day').forEach(d => d.classList.remove('selected'));
  el.classList.add('selected');
  state.selectedDate = date;

  document.getElementById('selectedDateLabel').textContent = date.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
  document.getElementById('timeSlotsSection').style.display = 'block';
  renderTimeSlots(date);
  updateOsDetails();
}

function renderTimeSlots(date) {
  const grid = document.getElementById('timeSlotsGrid');
  grid.innerHTML = '';
  state.selectedTime = null;
  document.getElementById('scheduleNext').disabled = true;

  ALL_TIMES.forEach((slot, idx) => {
    const isUnavail = !slot.avail || (date.getDate() % 2 === 0 && idx === 2);
    const el = document.createElement('div');
    el.className = 'time-slot' + (isUnavail ? ' slot-unavailable' : '');
    el.textContent = slot.t;
    if (!isUnavail) el.addEventListener('click', () => selectTime(slot.t, el));
    grid.appendChild(el);
  });
}

function selectTime(time, el) {
  document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
  el.classList.add('selected');
  state.selectedTime = time;
  document.getElementById('scheduleNext').disabled = false;
  updateOsDetails();
}

function prevMonth() { if (state.calMonth === 0) { state.calMonth = 11; state.calYear--; } else state.calMonth--; renderCalendar(); }
function nextMonth() { if (state.calMonth === 11) { state.calMonth = 0; state.calYear++; } else state.calMonth++; renderCalendar(); }

function updateOsDetails() {
  const osDetails = document.getElementById('osDetails');
  if (!osDetails) return;
  let html = `<strong>Frequency:</strong> ${state.frequency}`;
  if (state.selectedDate) html += `<br/><strong>Date:</strong> ${state.selectedDate.toLocaleDateString('en-GB', { weekday:'short',day:'numeric',month:'short' })}`;
  if (state.selectedTime) html += ` at ${state.selectedTime}`;
  osDetails.classList.add('visible');
  osDetails.innerHTML = html;
}

function formatCardNumber(el) { el.value = el.value.replace(/\D/g, '').substring(0, 16).replace(/(.{4})/g, '$1 ').trim(); }
function formatExpiry(el) { let v = el.value.replace(/\D/g, '').substring(0, 4); if (v.length >= 2) v = v.substring(0,2) + '/' + v.substring(2); el.value = v; }

function processPayment() {
  const num = document.getElementById('cardNumber')?.value?.replace(/\s/g,'');
  if (!num || num.length < 16) { showToast('Valid card number required.', 'error'); return; }

  const btn = document.getElementById('payBtn');
  btn.disabled = true;
  document.getElementById('payBtnText').textContent = 'Processing...';

  setTimeout(() => completeBooking('BK-' + Math.random().toString(36).substring(2,6).toUpperCase() + '-' + Date.now().toString().slice(-4)), 1500);
}

function completeBooking(ref) {
  const email = document.getElementById('email')?.value || 'customer@email.com';
  document.getElementById('confirmRef').textContent = ref;
  document.getElementById('confirmEmail').textContent = email;

  const total = Math.max(state.basePrice + state.bedroomAdjust + state.extrasPrice, 0);
  const dateStr = state.selectedDate ? state.selectedDate.toLocaleDateString('en-GB', { weekday:'long',day:'numeric',month:'long',year:'numeric' }) : 'TBC';

  document.getElementById('confirmSummaryCard').innerHTML = `
    <div style="font-size:0.95rem;line-height:1.6;">
      <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
        <span style="color:var(--text-muted)">Service</span>
        <strong>${state.serviceLabel}</strong>
      </div>
      <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
        <span style="color:var(--text-muted)">Schedule</span>
        <strong>${dateStr} at ${state.selectedTime}</strong>
      </div>
      <div style="border-top:1px solid var(--border-light);padding-top:12px;margin-top:12px;display:flex;justify-content:space-between;font-size:1.1rem;">
        <span>Total</span>
        <strong style="color:var(--text-main)">£${total}</strong>
      </div>
    </div>`;

  const bookings = JSON.parse(localStorage.getItem('cleaningBookings') || '[]');
  bookings.unshift({
    ref, service: state.serviceLabel, date: dateStr, time: state.selectedTime,
    customer: `${document.getElementById('firstName')?.value || ''} ${document.getElementById('lastName')?.value || ''}`.trim(),
    email, address: `${document.getElementById('addr1')?.value || ''}, ${document.getElementById('city')?.value || ''} ${document.getElementById('postcodeDetail')?.value || ''}`.replace(/^, /, ''),
    total, status: 'Confirmed', created: new Date().toISOString(), notes: document.getElementById('notes')?.value || '', phone: document.getElementById('phone')?.value || ''
  });
  localStorage.setItem('cleaningBookings', JSON.stringify(bookings));

  goStep(5);
}

function downloadInvoice() { window.open('invoice.html', '_blank'); }

document.addEventListener('DOMContentLoaded', () => {
  initCalendar();
  const params = new URLSearchParams(window.location.search);
  const svcParam = params.get('service');
  if (svcParam) {
    const card = document.querySelector(`[data-svc="${svcParam}"]`);
    if (card) {
      const map = { deep:120, regular:70, eot:150, ironing:25, oven:65, movein:130 };
      const labels = { deep:'Deep Cleaning', regular:'Regular Cleaning', eot:'End of Tenancy', ironing:'Ironing', oven:'Oven Cleaning', movein:'Move In' };
      selectService(card, svcParam, labels[svcParam], map[svcParam] || 70);
    }
  }
});
