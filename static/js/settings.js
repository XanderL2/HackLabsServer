
const container = document.querySelector(".container");
const closeBox = document.querySelector(".close-box");
const btnSave = document.querySelector(".btn-save");
const savedBox = document.querySelector(".saved-box");
const select = document.querySelector("select");
const option1 = document.querySelector(".option1");
const option2 = document.querySelector(".option2");
const option3 = document.querySelector(".option3");

const settingsP = document.querySelector(".settingsP");
const closeP = document.querySelector(".closeP");
const languageP = document.querySelector(".languageP");
const languagePP = document.querySelector(".languagePP");
const autoplayP = document.querySelector(".autoplayP");
const autoplayPP = document.querySelector(".autoplayPP");
const showP = document.querySelector(".showP");
const showPP = document.querySelector(".showPP");
const btnCancel = document.querySelector(".btn-cancel");
const savedP = document.querySelector(".savedP");


closeBox.addEventListener("click", () =>{
    container.classList.remove("open");
    container.classList.add("close");
    setTimeout(() =>{
        container.classList.remove("close");
        container.classList.add("open");
    }, 1500)
})

select.addEventListener("change", function () {
    const selectedValue = select.value;
  
    if (selectedValue === "IT") {
      settingsP.innerHTML = "Impostazioni";
      closeP.innerHTML = "Chiudi";
      languageP.innerHTML = "Lingua";
      languagePP.innerHTML = "Facci sapere con quale lingua ti senti più a tuo agio. Puoi cambiarla di nuovo in qualsiasi momento.";
      autoplayP.innerHTML = "Video a riproduzione automatica";
      autoplayPP.innerHTML = "Scegli se desideri riprodurre automaticamente nel tuo browser.";
      showP.innerHTML = "Mostra le foto del profilo";  
      showPP.innerHTML = "Scegli se mostrare o meno le foto del profilo degli altri membri.";  
      btnSave.innerHTML = "Salva";
      btnCancel.innerHTML = "Cancella";
      savedP.innerHTML = "Salvato!"
    } else if (selectedValue === "ES") {
        settingsP.innerHTML = "Configuración";
        closeP.innerHTML = "Cerrar";
        languageP.innerHTML = "Idioma";
        languagePP.innerHTML = "Indícanos en qué idioma te sientes más cómodo. Puedes cambiarlo en cualquier momento.";
        autoplayP.innerHTML = "Reproducción automática de videos.";
        autoplayPP.innerHTML = "Elige si deseas reproducir automáticamente los videos en tu navegador.";
        showP.innerHTML = "Mostrar fotos de perfil.";  
        showPP.innerHTML = "Elige si deseas mostrar o no las fotos de perfil de otros miembros.";  
        btnSave.innerHTML = "Guardar";
        btnCancel.innerHTML = "Cancelar"; 
        savedP.innerHTML = "Guardado!"
    } else if (selectedValue === "EN") {
        settingsP.innerHTML = "Settings";
        closeP.innerHTML = "Close";
        languageP.innerHTML = "Language";
        languagePP.innerHTML = "Let us know which language you're most comfortable using. You can change it back at any time.";
        autoplayP.innerHTML = "Autoplay videos.";
        autoplayPP.innerHTML = "Choose if you want to autoplay on your browser.";
        showP.innerHTML = "Show profile photos.";  
        showPP.innerHTML = "Choose whether to show or hide profile photos of other members.";  
        btnSave.innerHTML = "Save";
        btnCancel.innerHTML = "Cancel";
        savedP.innerHTML = "Saved!"
    }
  });  
  
  
  
  
  


btnSave.addEventListener("click", () =>{
    savedBox.style.display = "block";
    setTimeout(()=>{
        savedBox.style.display = "none";
    }, 2000)
})
