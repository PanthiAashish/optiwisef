// components/AuthButton.tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { signInWithGoogle, logout, auth } from "../firebase/auth";
import { onAuthStateChanged } from "firebase/auth";

const AuthButton = () => {
  const [user, setUser] = useState(null);
  const router = useRouter();

  // Listen to authentication state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
      if (currentUser) {
        // Redirect to localhost:8501 when authentication is successful
        router.push("http://localhost:8501/");
      }
    });

    return () => unsubscribe(); // Cleanup listener on component unmount
  }, [router]);

  return (
    <div className="w-full max-w-sm">
      {user ? (
        <>
          <p className="text-lg mb-4">Welcome, {user.displayName}</p>
          <button
            onClick={logout}
            className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-800"
          >
            Logout
          </button>
        </>
      ) : (
        <div className="space-y-4">
          <input
            type="email"
            placeholder="Email*"
            className="w-full border border-gray-300 p-2 rounded-md"
          />
          <input
            type="password"
            placeholder="Password*"
            className="w-full border border-gray-300 p-2 rounded-md"
          />
          <button className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-800">
            Sign Up
          </button>
          <button className="w-full bg-black text-white py-2 rounded-md hover:bg-gray-800">
            Log In
          </button>
          <button
            onClick={signInWithGoogle}
            className="w-full border border-black py-2 flex justify-center items-center space-x-2 rounded-md hover:bg-gray-100"
          >
            <span className="text-black">G</span>
            <span>Log in with Google</span>
          </button>
          <a href="#" className="text-sm text-blue-600 hover:underline">
            Forgot your password?
          </a>
        </div>
      )}
    </div>
  );
};

export default AuthButton;
