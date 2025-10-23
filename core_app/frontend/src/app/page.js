import Image from "next/image";
import Link from "next/link";
import { Button } from "@/components/ui/button";
export default function Home() {
    return (
        <div className="  min-h-screen  flex flex-col justify-center items-center content-around bg-zinc-50  font-sans ">
            <div className="text-center mb-10 mb-[10rem]">
                <h1 className="text-4xl font-bold text-gray-800 mb-2">Quizzler</h1>
                <p className="text-gray-600">
                    {" "}
                    A modern academic experience for teachers and students
                </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-3xl">
                <div className="bg-white shadow-lg rounded-2xl p-6 text-center">
                    <h2 className="text-2xl font-semibold mb-4 text-gray-800">
                        For Teachers
                    </h2>
                    <p className="text-gray-600 mb-6">
                        Create and manage your classes effortlessly.
                    </p>
                    <div className="flex justify-center gap-4">
                        <Link href="/teachers/login">
                            <Button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg">
                                Login
                            </Button></Link>
                        <Link href="/teachers/signup"><Button className="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-lg">
                            Sign Up
                        </Button></Link>
                    </div>
                </div>
                <div className="bg-white shadow-lg rounded-2xl p-6 text-center">
                    <h2 className="text-2xl font-semibold mb-4 text-gray-800">
                        For Students
                    </h2>
                    <p className="text-gray-600 mb-6">
                        Join your classes and stay organized.
                    </p>
                    <div className="flex justify-center gap-4">
                        <Link href="/students/login"><Button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg">
                            Login
                        </Button></Link>
                        <Link href="/students/signup"><Button className="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-lg">
                            Sign Up
                        </Button></Link>
                    </div>
                </div>
            </div>
        </div>
    );
}
