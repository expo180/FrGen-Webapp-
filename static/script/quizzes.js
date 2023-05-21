// Questions et réponses du quiz
const questions = [
    {
      question: "Question 1: Quelle est la capitale de la France ?",
      answers: {
        a: "Paris",
        b: "Londres",
        c: "Berlin"
      },
      correctAnswer: "a"
    },
    {
      question: "Question 2: Combien font 2 + 2 ?",
      answers: {
        a: "3",
        b: "4",
        c: "5"
      },
      correctAnswer: "b"
    },
    // Ajoutez d'autres questions ici...
  ];
  
  // Fonction pour afficher les questions et les réponses possibles
  function afficherQuestions() {
    const quizContainer = document.getElementById("quiz-container");
    const resultsContainer = document.getElementById("results-container");
    const submitButton = document.getElementById("submit-button");
  
    // Générer le code HTML pour chaque question
    const output = [];
    questions.forEach((question, questionIndex) => {
      // Stocker les réponses possibles
      const answers = [];
      for (const option in question.answers) {
        answers.push(
          `<label>
            <input type="radio" name="question${questionIndex}" value="${option}">
            ${option}: ${question.answers[option]}
          </label>`
        );
      }
  
      // Ajouter la question et les réponses à la sortie
      output.push(
        `<div class="question">${question.question}</div>
         <div class="answers">${answers.join("")}</div>`
      );
    });
  
    // Afficher les questions et les réponses possibles
    quizContainer.innerHTML = output.join("");
  
    // Ajouter un gestionnaire d'événement pour le bouton de soumission
    submitButton.addEventListener("click", afficherRésultats);
  }
  
  // Fonction pour afficher les résultats du quiz
  function afficherRésultats() {
    const quizContainer = document.getElementById("quiz-container");
    const resultsContainer = document.getElementById("results-container");
  
    // Récupérer les réponses de l'utilisateur
    const answerContainers = quizContainer.getElementsByClassName("answers");
    let score = 0;
  
    questions.forEach((question, questionIndex) => {
      const answerContainer = answerContainers[questionIndex];
      const selector = `input[name=question${questionIndex}]:checked`;
      const userAnswer = (answerContainer.querySelector(selector) || {}).value;
  
      // Vérifier la réponse de l'utilisateur et incrémenter le score si correct
      if (userAnswer === question.correctAnswer) {
        score++;
      }
    });
  
    // Afficher le score final
    resultsContainer.innerHTML = `Score: ${score} / ${questions.length}`;
  
    // Masquer le conteneur des questions et afficher le conteneur des résultats
    quizContainer.style.display = "none";
    resultsContainer.style.display = "block";
  }
  
  // Démarrer le quiz lorsque la page est chargée
  window.addEventListener("load", afficherQuestions);
  
