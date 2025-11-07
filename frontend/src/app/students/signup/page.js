import AuthLayout from "@/components/AuthPages";
import { auth, users } from "@/lib/constants";
export default function Page() {
    return (
        <>
            <AuthLayout type={auth.signup} user={users.students} />
        </>
    );
}
