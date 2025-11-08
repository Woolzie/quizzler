"use client";
import React, {
    createContext,
    ReactNode,
    useContext,
    useEffect,
    useState,
} from "react";

type ILogin = {
    username: string;
    password: string;
};
interface IAuthContext {
    username: string;
    login: (val: ILogin) => Promise<boolean>;
}
interface Props {
    children: React.ReactNode;
}

const AuthContext = createContext<IAuthContext | null>(null);

export const AuthProvider = ({ children }: any) => {
    const [username, setUsername] = useState("");

    //TODO: fix this so it only calls in the beginning
    useEffect(() => {
        const saved = localStorage.getItem("user");
        if (saved) setUsername(JSON.parse(saved));
    }, []);

    // Handle user login
    const login = async ({ username, password }: ILogin) => {
        const res = await fetch("http://localhost:8000/api/v1/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });

        if (res.ok) {
            const user = await res.json();
            setUsername(user);
            localStorage.setItem("user", JSON.stringify(user));
            return true;
        }
        return false;
    };

    const value: IAuthContext = {
        username,
        login,
    };
    return (
        <AuthContext value={value}>
            {children}
        </AuthContext>
    );
};

export const useAuth = () => useContext(AuthContext);
