"use client";
// import styles from "@/app/styles/dashboard.css";
import "./../styles/dashboard.css";
import Card from "./../components/Card.tsx";

export default function Home() {
    const teacherClick = () => {
        //TODO: check local storage if they are logged in
        console.log("meow");
    };
    const studentClick = () => {
        console.log("meow");
    };
    return (
        <div className="h-screen w-screen ">
            <h1 className="heading">
                Quizzler
            </h1>
            <div className="h-full w-full flex justify-center items-center gap-7">
                <Card
                    header={"Teachers"}
                    content={"Grade your students with ease"}
                    handleClick={teacherClick}
                />
                <Card
                    header={"Students"}
                    content={"Test your knowledge with confidence"}
                    handleClick={studentClick}
                />
            </div>
        </div>
    );
}
