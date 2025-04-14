const selectionModal = document.getElementById("selectionModal");
const detailModal = document.getElementById("detailModal");
const systemModal = document.getElementById("systemModal");
const motormodal = document.getElementById("motormodal");
const ActualdataModal = document.getElementById("ActualdataModal");
const ElectricalModal = document.getElementById("ElectricalModal");
const CommercialdataModal = document.getElementById("CommercialdataModal");
const TestcurveModal = document.getElementById("TestcurveModal");

const showModalBtn = document.getElementById("showModalBtn");
const openPumpModal = document.getElementById("openPumpModal");
const opensystemModal = document.getElementById("opensystemModal");
const openMotorModal = document.getElementById("openmotormodal");
const openActualModal = document.getElementById("openActulModal");
const openCommercialModal = document.getElementById("opencommercialModal");
const openElectricalModal = document.getElementById("openElectricalModal");
const openTestCurveModal = document.getElementById("opentestcueveModal");

const closeDetailModal = document.getElementById("closeDetailModal");
const savePumpData = document.getElementById("savePumpData");

// Open selection modal
showModalBtn?.addEventListener("click", () => {
    selectionModal.style.display = "flex";
});

// Modal open handlers
openPumpModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    detailModal.style.display = "flex";
});

opensystemModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    systemModal.style.display = "flex";
});

openMotorModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    motormodal.style.display = "flex";
});

openActualModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    ActualdataModal.style.display = "flex";
});

openElectricalModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    ElectricalModal.style.display = "flex";
});

openCommercialModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    CommercialdataModal.style.display = "flex";
});

openTestCurveModal?.addEventListener("click", () => {
    selectionModal.style.display = "none";
    TestcurveModal.style.display = "flex";
});

// Close all modals
closeDetailModal?.addEventListener("click", () => {
    detailModal.style.display = "none";
    systemModal.style.display = "none";
    motormodal.style.display = "none";
    ActualdataModal.style.display = "none";
    ElectricalModal.style.display = "none";
    CommercialdataModal.style.display = "none";
    TestcurveModal.style.display = "none";
});

// Save action (customize as needed)
savePumpData?.addEventListener("click", () => {
    alert("Pump data saved!");
    detailModal.style.display = "none";
});
