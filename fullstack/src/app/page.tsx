// page.tsx
import AuthButton from "./components/AuthButton";

export default function Home() {
  return (
    <div className="min-h-screen flex">
      {/* Left Section */}
      <div className="w-1/2 bg-gray-100 flex flex-col justify-center items-center p-10">
        <h1 className="text-4xl font-bold mb-4">OptiWise</h1>
        <p className="text-lg text-gray-600">
          Empowering Investors with advanced option pricing tools
        </p>
      </div>

      {/* Right Section */}
      <div className="w-1/2 flex flex-col justify-center items-center p-10">
        <h2 className="text-3xl font-bold mb-6">Log In</h2>
        <p className="mb-6 text-gray-500">Join OptiWise</p>
        <AuthButton />
      </div>

      {/* Test */}
      <p className="text-red-50">Red</p>
    </div>
  );
}
