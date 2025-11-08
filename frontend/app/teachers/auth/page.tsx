"use client";
import { Login } from "@/components/Login";
import { useAuth } from "context/AuthContext";
import { useEffect, useState } from "react";

export default function StudentLogin() {
    const [formData, setFormData] = useState({ username: "", password: "" });
    const { login } = useAuth();
    const [isLoading, setLoading] = useState(false);
    useEffect(() => {
        async function Login() {
            return await login(formData);
        }
        if (isLoading) {
            const res = Login();
            console.log(`logged in ${res}`);
        }
    }, [isLoading]);
    const handleSubmit = (e: React.FormEvent<HTMLInputElement>) => {
        e.preventDefault();
        setLoading(true);
    };
    const handleChange = (e: React.FormEvent<HTMLInputElement>) => {
        setFormData({
            ...formData,
            [e.currentTarget.name]: e.currentTarget.value,
        });
    };
    return (
        <div>
            <h1 className="text-center text-4xl mt-17">Hello there Teacher</h1>
            <Login
                formData={formData}
                handleChange={handleChange}
                handleSubmit={handleSubmit}
            />
        </div>
    );
}
