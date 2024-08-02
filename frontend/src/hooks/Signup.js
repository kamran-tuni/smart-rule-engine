import { useState } from 'react';
import { apiEndpoints, appEndpoints } from '../config/Endpoints';

import Cookies from 'js-cookie';


const useSignup = () => {
    const signup = async (data, setIsLoading, setMessage, setTabIndex) => {
   		try {
            const response = await fetch(apiEndpoints.signup, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                const _message = 'Registration successful with IoT Platform Integration. Login now!'

                setMessage({'severity': 'success', 'content': _message});
                setTabIndex(0);
            } else {
                throw new Error('Signup failed');
            }
        } catch (error) {
            setMessage({'severity': 'error', 'content': error.message});
        } finally {
            setIsLoading(false);
        }
    };

    return { signup };
};

export default useSignup;

