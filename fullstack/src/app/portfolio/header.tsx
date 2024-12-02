"use client";
import { signInWithPopup, signOut } from "firebase/auth";
import { auth, googleProvider } from "../firebase/config";

const Header = ({ user, setUser }) => {
  const handleGoogleSignIn = async () => {
    try {
      const result = await signInWithPopup(auth, googleProvider);
      setUser(result.user); // Notify parent about user login
    } catch (error) {
      console.error("Error signing in with Google: ", error);
    }
  };

  const handleSignOut = async () => {
    try {
      await signOut(auth);
      setUser(null); // Notify parent about user logout
    } catch (error) {
      console.error("Error signing out: ", error);
    }
  };

  const getInitials = (name) => {
    if (!name) return "";
    const names = name.split(" ");
    const initials = names.map((n) => n[0].toUpperCase()).join("");
    return initials;
  };

  return (
    <header
      style={{
        display: "flex",
        justifyContent: "flex-end",
        alignItems: "center",
        padding: "10px 20px",
        backgroundColor: "#f5f5f5",
        borderBottom: "1px solid #ddd",
      }}
    >
      {!user ? (
        <button
          onClick={handleGoogleSignIn}
          style={{
            padding: "8px 16px",
            fontSize: "14px",
            cursor: "pointer",
            borderRadius: "4px",
            border: "none",
            backgroundColor: "#4285F4",
            color: "#fff",
          }}
        >
          Sign in with Google
        </button>
      ) : (
        <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              width: "40px",
              height: "40px",
              borderRadius: "50%",
              backgroundColor: "#4285F4",
              color: "#fff",
              fontSize: "16px",
              fontWeight: "bold",
            }}
          >
            {getInitials(user.displayName)}
          </div>
          <button
            onClick={handleSignOut}
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              cursor: "pointer",
              borderRadius: "4px",
              border: "none",
              backgroundColor: "#DB4437",
              color: "#fff",
            }}
          >
            Sign Out
          </button>
        </div>
      )}
    </header>
  );
};

export default Header;
