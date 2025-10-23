import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";

function AuthLayout({ title, type, user }) {
	const basePath = user === "teacher" ? "/teachers" : "/students";
	return (
		<main className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
			<div className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-md text-center">
				<h1 className="text-3xl font-bold text-gray-800 mb-6">{title}</h1>
				<form className="flex flex-col gap-4">
					{type === "signup" && (
						<input
							type="text"
							placeholder="Full Name"
							className="border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					)}
					<input
						type="email"
						placeholder="Email"
						className="border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
					/>
					<input
						type="password"
						placeholder="Password"
						className="border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
					/>
					<Button className="bg-blue-600 hover:bg-blue-700 text-white w-full py-2 rounded-lg mt-4">
						{type === "login" ? "Login" : "Create Account"}
					</Button>
				</form>

				<div className="mt-6 text-gray-600">
					{type === "login" ? (
						<p>
							Don’t have an account?{" "}
							<Link
								href={`${basePath}/signup`}
								className="text-blue-600 hover:underline"
							>
								Sign up
							</Link>
						</p>
					) : (
						<p>
							Already have an account?{" "}
							<Link
								href={`${basePath}/signup`}
								className="text-blue-600 hover:underline"
							>
								Login
							</Link>
						</p>
					)}
				</div>
			</div>
		</main>
	);
}
export function TeacherLogin() {
	return <AuthLayout title="Teacher Login" type="login" user={"teacher"} />;
}

// Teacher Signup Page
export function TeacherSignup() {
	return <AuthLayout title="Teacher Sign Up" type="signup" user={"teacher"} />;
}

// Student Login Page
export function StudentLogin() {
	return <AuthLayout title="Student Login" type="login" user={"student"} />;
}

// Student Signup Page
export function StudentSignup() {
	return <AuthLayout title="Student Sign Up" type="signup" user={"student"} />;
}
