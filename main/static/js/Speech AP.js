const voiceBtn = document.getElementById("voicebtn");
const searchInput = document.getElementById("searchinput");

const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
    alert("Ваш браузер не підтримує голосовий ввід");
} else {
    const recognition = new SpeechRecognition();
    recognition.lang = "uk-UA";
    recognition.interimResults = false;

    voiceBtn.addEventListener("click", () => {
        recognition.start();
    });

    recognition.onresult = (event) => {
        const text = event.results[0][0].transcript;
        searchInput.value = text;
    };

    recognition.onerror = (event) => {
        console.error("Помилка:", event.error);
    };
}
