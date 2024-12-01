// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyABhHApYeC6vlWIAL29cqUoqTLqz8-sg9I",
  authDomain: "optiwise-7f66f.firebaseapp.com",
  projectId: "optiwise-7f66f",
  storageBucket: "optiwise-7f66f.firebasestorage.app",
  messagingSenderId: "1036620684969",
  appId: "1:1036620684969:web:011dc1ef3c0311732193b8",
  measurementId: "G-5X2T6LX95E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);