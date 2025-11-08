import "@/styles/globals.css";

type Form = {
    readonly username: string;
    readonly password: string;
};
interface LoginProps {
    formData: Form;
    handleChange: (e: React.FormEvent<HTMLInputElement>) => void;
    handleSubmit: (e: React.FormEvent<HTMLInputElement>) => void;
}
const Login = ({ formData, handleChange, handleSubmit }: LoginProps) => {
    return (
        <div className="w-screen h-screen">
            <div className="flex flex-col justify-evenly items-center border-card-border border-4 w-[35%] h-[40%] m-auto mt-15 p-5 gap-5 rounded-3xl">
                <h1 className="text-3xl font-bold">Login</h1>
                <form className="flex flex-col justify-center items-center gap-5 w-full h-full">
                    <input
                        type="text"
                        name="username"
                        onInput={handleChange}
                        placeholder="Name"
                        value={formData.username}
                        className="border-2 w-full p-2 focus:border-input-border"
                        required
                    />

                    <input
                        type="password"
                        name="password"
                        onInput={handleChange}
                        placeholder="••••••••"
                        value={formData.password}
                        className="border-2  w-full p-2 focus:border-input-border"
                        required
                    />
                    <button
                        className="bg-primary-button rounded-xl p-5"
                        onClick={handleSubmit}
                    >
                        Submit
                    </button>
                </form>
            </div>
        </div>
    );
};
export { Login };
