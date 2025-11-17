"use client";
import React, { useEffect, useRef, useState } from "react";
import { Bot, Send, Sparkles, User } from "lucide-react";
import "@/styles/room.css";

export default function ChatBot() {
    const [messages, setMessages] = useState([
        {
            role: "assistant",
            content: "Hello! I'm your AI assistant. How can I help you today?",
        },
    ]);
    const [input, setInput] = useState("");
    const [isTyping, setIsTyping] = useState(false);
    const messagesEndRef = useRef(null);
    const textareaRef = useRef(null);
    const [isFocused, setFocused] = useState(false);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isTyping]);

    useEffect(() => {
        if (!isFocused) textareaRef.current.focus();
        setFocused(true);
    });
    useEffect(() => {
        if (textareaRef.current) {
            textareaRef.current.style.height = "auto";
            textareaRef.current.style.height =
                textareaRef.current.scrollHeight + "px";
        }
    }, [input]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!input.trim() || isTyping) return;

        const userMessage = input.trim();
        setInput("");
        setMessages(
            (prev) => [...prev, { role: "user", content: userMessage }],
        );
        setIsTyping(true);

        // Simulate AI response
        setTimeout(() => {
            const responses = [
                "That's an interesting question! Let me think about that...",
                "I understand what you're asking. Here's my perspective...",
                "Great question! Based on what you've told me...",
                "I'd be happy to help with that. Let me explain...",
                "That's a common concern. Here's what I think...",
            ];
            const randomResponse =
                responses[Math.floor(Math.random() * responses.length)];
            setMessages(
                (prev) => [...prev, {
                    role: "assistant",
                    content: randomResponse,
                }],
            );
            setIsTyping(false);
        }, 1500);
    };

    const handleKeyDown = (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    return (
        <div className="flex flex-col h-[95vh] ">
            {/* Messages */}
            <div className="flex-1 overflow-y-auto px-4 py-6 space-y-6 room-bg">
                {messages.map((msg, idx) => (
                    <div
                        key={idx}
                        className={`flex gap-4 ${
                            msg.role === "user"
                                ? "justify-end"
                                : "justify-start"
                        }`}
                    >
                        {msg.role === "assistant" && (
                            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
                                <Bot className="w-5 h-5 text-white" />
                            </div>
                        )}
                        <div
                            className={`max-w-3xl ${
                                msg.role === "user" ? "order-first" : ""
                            }`}
                        >
                            <div
                                className={`rounded-2xl px-5 py-3 ${
                                    msg.role === "user"
                                        ? "bg-slate-600 text-white ml-auto"
                                        : "bg-gray-800/80 text-gray-100 backdrop-blur-sm"
                                }`}
                            >
                                <p className="text-sm leading-relaxed whitespace-pre-wrap">
                                    {msg.content}
                                </p>
                            </div>
                        </div>
                        {msg.role === "user" && (
                            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center">
                                <User className="w-5 h-5 text-gray-300" />
                            </div>
                        )}
                    </div>
                ))}

                {isTyping && (
                    <div className="flex gap-4 justify-start">
                        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
                            <Bot className="w-5 h-5 text-white" />
                        </div>
                        <div className="max-w-3xl">
                            <div className="rounded-2xl px-5 py-3 bg-gray-800/80 backdrop-blur-sm">
                                <div className="flex gap-1">
                                    <div
                                        className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                                        style={{ animationDelay: "0ms" }}
                                    >
                                    </div>
                                    <div
                                        className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                                        style={{ animationDelay: "150ms" }}
                                    >
                                    </div>
                                    <div
                                        className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                                        style={{ animationDelay: "300ms" }}
                                    >
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input */}
            <div className="border-t border-gray-700/50 bg-gray-800/50 backdrop-blur-sm px-4 py-4">
                <div className="max-w-4xl mx-auto">
                    <div className="relative">
                        <textarea
                            ref={textareaRef}
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Send a message..."
                            rows={1}
                            className="w-full bg-gray-900/50 text-white placeholder-gray-500 rounded-xl pl-5 pr-12 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500/50 resize-none max-h-32 border border-gray-700/50"
                        />
                        <button
                            onClick={handleSubmit}
                            disabled={!input.trim() || isTyping}
                            className="absolute right-2 bottom-2 p-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 disabled:cursor-not-allowed rounded-lg transition-colors"
                        >
                            <Send className="w-4 h-4 text-white" />
                        </button>
                    </div>
                    <p className="text-xs text-gray-500 text-center mt-3">
                        Press Enter to send, Shift+Enter for new line
                    </p>
                </div>
            </div>
        </div>
    );
}
