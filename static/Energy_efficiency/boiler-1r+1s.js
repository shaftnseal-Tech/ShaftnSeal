const selectionModal = document.getElementById("selectionModal");
const detailModal = document.getElementById("detailModal");

const showModalBtn = document.getElementById("showModalBtn");
const openPumpModal = document.getElementById("openPumpModal");
const closeDetailModal = document.getElementById("closeDetailModal");
const savePumpData = document.getElementById("savePumpData");
const openmotormodal=document.getElementById("openmotormodal");
const openActulModal=document.getElementById("openActulModal");
const opencommercialModal=document.getElementById("opencommercialModal");
const openElectricalModal=document.getElementById("openElectricalModal")
const opentestcueveModal=document.getElementById("opentestcueveModal")
// Open selection modal
showModalBtn.addEventListener("click", () => {
    selectionModal.style.display = "flex";
});

// When user selects "Pump Name Plate Data"
openPumpModal.addEventListener("click", () => {
    selectionModal.style.display = "none";
    detailModal.style.display = "flex";
});
openmotormodal.addEventListener(
"click",()=>{
    selectionModal.style.display='none';
  motormodal.style.display="flex"
}
)
openActulModal.addEventListener("click",()=>{
 selectionModal.style.display="none";
 ActualdataModal.style.display="flex"
})

openElectricalModal.addEventListener("click",()=>{
selectionModal.style.display="none";
ElectricalModal.style.display="flex"
})
opencommercialModal.addEventListener("click",()=>{
    selectionModal.style.display="none";
    CommercialdataModal.style.display="flex"
})
opentestcueveModal.addEventListener("click",()=>{
selectionModal.style.display="none";
TestcurveModal.style.display="flex"
})


// Close detail modal
closeDetailModal.addEventListener("click", () => {
    detailModal.style.display = "none";
    CommercialdataModal.style.display="none";
    ElectricalModal.style.display="none";
    ActualdataModal.style.display="none";
    motormodal.style.display="none";
    TestcurveModal.style.display="none"
});


// Save button (you can add logic here)
savePumpData.addEventListener("click", () => {
    alert("Pump data saved!");
    detailModal.style.display = "none";
});