// Liste de mots à deviner
const words = ["Junior"];

// Mot aléatoire à deviner
const randomIndex = Math.floor(Math.random() * words.length);
const wordToGuess = words[randomIndex];
let guessedWord = Array(wordToGuess.length).fill("_");

// Nombre de tentatives restantes
let remainingAttempts = 6;

// Fonction pour afficher le mot à deviner et les lettres déjà devinées
function displayWord() {
  document.getElementById("wordDisplay").textContent = guessedWord.join(" ");
}

// Fonction pour afficher les tentatives restantes
function displayGuesses() {
  document.getElementById("guesses").textContent = `Tentatives restantes: ${remainingAttempts}`;
}

// Fonction pour vérifier si la lettre est dans le mot
function guessLetter() {
  const letterInput = document.getElementById("letterInput");
  const guessedLetter = letterInput.value.toLowerCase();

  if (guessedLetter.length !== 1) {
    alert("Veuillez entrer une seule lettre.");
    return;
  }

  if (wordToGuess.includes(guessedLetter)) {
    for (let i = 0; i < wordToGuess.length; i++) {
      if (wordToGuess[i] === guessedLetter) {
        guessedWord[i] = guessedLetter;
      }
    }
  } else {
    remainingAttempts--;
  }

  displayWord();
  displayGuesses();

  letterInput.value = "";

  if (guessedWord.join("") === wordToGuess) {
    alert("Félicitations, vous avez deviné le mot !");
  } else if (remainingAttempts === 0) {
    alert("Désolé, vous avez épuisé toutes vos tentatives. Le mot était : " + wordToGuess);
  }
}

// Initialisation de l'affichage
displayWord();
displayGuesses();

  