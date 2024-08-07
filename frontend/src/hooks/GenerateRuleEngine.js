import { useState } from 'react';
import { apiEndpoints, appEndpoints } from '../config/Endpoints';
import Cookies from 'js-cookie';


const useGenerateRuleEngine = () => {
    const generateRuleEngine = async (data, setIsLoading, setMessages) => {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 40000);

        try {
            const csrfToken = Cookies.get('csrftoken');
            const response = await fetch(apiEndpoints.ruleEngine, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
                credentials: 'include',
                signal: controller.signal
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                const errorData = await response.json();
                setIsLoading(false);
                return;
            }

            const response_data = await response.json();
            setIsLoading(false);
            setMessages(response_data["chat_history"]);
        } catch (error) {
            clearTimeout(timeoutId);
            if (error.name === 'AbortError') {
                throw new Error('Request timeout: Please try again.');
            } else {
                throw new Error('Error generating rule engine');
            }
            setIsLoading(false);
        }
    };

    return { generateRuleEngine };
};

export default useGenerateRuleEngine;
