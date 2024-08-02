import { useState } from 'react';
import { apiEndpoints, appEndpoints } from '../config/Endpoints';

import Cookies from 'js-cookie';


const useLogin = () => {
    const login = async (accountId, data, setIsLoading, setMessage) => {
        Cookies.set('tenant', accountId, { expires: 30 });

        try {
            const response = await fetch(apiEndpoints.login, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
                credentials: 'include'
            });

            if (response.ok) {
                window.location.href = appEndpoints.dashboard;
            } else {
                throw new Error("Account ID, Username or Password incorrect! Try again!");
            }
        } catch (error) {
            setMessage({'severity': 'error', 'content': error.message});
        } finally {
            setIsLoading(false);
        }
    };

    return { login };
};

export default useLogin;
