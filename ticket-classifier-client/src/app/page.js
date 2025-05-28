"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Loader2, Copy } from "lucide-react"
import { AnimatedPieChart } from "@/components/AnimatedPieChart"

const categoryData = [
    { name: "Technical Support", value: 10, color: "#4285F4" },
    { name: "Customer Service", value: 10, color: "#EA4335" },
    { name: "Billing and Payments", value: 10, color: "#FBBC05" },
    { name: "Product Support", value: 10, color: "#34A853" },
    { name: "IT Support", value: 10, color: "#673AB7" },
    { name: "Returns and Exchanges", value: 10, color: "#FF6D00" },
    { name: "Sales and Pre-Sales", value: 10, color: "#00BFA5" },
    { name: "Human Resources", value: 10, color: "#FF4081" },
    { name: "Service Outages and Maintenance", value: 10, color: "#9E9E9E" },
    { name: "General Inquiry", value: 10, color: "#795548" },
]

const priorityData = [
    { name: "High", value: 33.33, color: "#dc2626" },
    { name: "Medium", value: 33.33, color: "#ea580c" },
    { name: "Low", value: 33.33, color: "#65a30d" },
]

const sampleQueries = [
    "Dear Customer Support Team,\n\nI am reaching out to request an update on the structural details of our organization.\
    The current records reflect information about the marketing agency, which has recently experienced several significant changes.\
    To ensure our records accurately depict the current operations, I would appreciate your assistance in updating the information.\
    \n\nFirst, I would like to clarify the refined roles within the various departments of the agency.\
    Each department now has clearly defined responsibilities aimed at enhancing efficiency and accountability.\
    For instance, the Creative Department is now dedicated solely to content creation.",
    "Dear Customer Support Team,\n\nI hope this message finds you well.\
    I am reaching out to request clarification about the billing and payment procedures linked to my account.\
    Recently, I observed some inconsistencies in the charges applied and would like to ensure I fully understand the billing cycle,\
    accepted payment options, and any potential extra charges.\n\nFirstly, I would be grateful if you could provide a detailed explanation\
    of how the billing cycle functions. Specifically, I am interested in knowing the start and end dates.\
    \n\nThank you for your assistance regarding these billing inquiries.",
    "Dear Customer Support Team,\n\nI am writing to report a significant problem with the centralized account management portal,\
    which currently appears to be offline. This outage is blocking access to account settings, leading to substantial inconvenience.\
    I have attempted to log in multiple times using different browsers and devices, but the issue persists.\
    \n\nCould you please provide an update on the outage status and an estimated time for resolution?\
    Also, are there any alternative ways to access and manage my account during this downtime?",
]

export default function PredictionDashboard() {
    const [inputText, setInputText] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const [isDisabled, setIsDisabled] = useState(true)
    const [prediction, setPrediction] = useState(null)
    const [error, setError] = useState(null)

    const handleInputChange = (e) => {
        const input = e.target.value
        setInputText(input)

        if (!input.trim()) {
            setError("Input cannot be empty")
            setIsDisabled(true)
        } else if (input.trim().length < 20) {
            setError("Input must be at least 20 characters long")
            setIsDisabled(true)
        } else {
            setError(null)
            setIsDisabled(false)
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!inputText.trim() || inputText.length < 20) {
            setError("Input must be at least 20 characters long.")
            return
        }

        setIsLoading(true)
        setIsDisabled(true)
        setError(null)

        try {
            const response = await fetch(process.env.NEXT_PUBLIC_API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: inputText }),
            })

            if (!response.ok) throw new Error("Failed to get prediction")

            const result = await response.json()
            setPrediction(result)
        } catch {
            setError("Failed to get prediction. Please try again.")
        } finally {
            setIsLoading(false)
            setIsDisabled(false)
        }
    }

    const handleSampleClick = (sample) => {
        setInputText(sample)
        setIsDisabled(false)
        setError(null)
    }

    const copyToClipboard = (text) => {
        navigator.clipboard.writeText(text).catch(console.error)
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-4">
            <div className="max-w-6xl mx-auto space-y-8">
                {/* Header */}
                <div className="text-center space-y-2">
                    <h1 className="text-4xl font-bold text-slate-900">Smart Ticket Routing with AI</h1>
                    <p className="text-slate-600 text-lg">
                        Enter a support query to get real-time predictions for <strong>Category</strong> and <strong>Priority</strong> — visualized through intelligent analytics
                    </p>
                </div>
                {/* Input Form */}
                <Card className="shadow-lg">
                    <CardHeader>
                        <CardTitle>Input Query</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div className="flex flex-col gap-4 md:flex-row">
                                <Textarea
                                    value={inputText}
                                    onChange={handleInputChange}
                                    placeholder="Enter your text here..."
                                    className="flex-1"
                                    disabled={isLoading}
                                />
                                <Button type="submit" disabled={isDisabled || isLoading} className="px-8">
                                    {isLoading ? (
                                        <>
                                            <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                                            Analyzing...
                                        </>
                                    ) : (
                                        "Predict"
                                    )}
                                </Button>
                            </div>
                            {error && <p className="text-red-600 text-sm">{error}</p>}
                        </form>
                    </CardContent>
                </Card>
                {/* Sample Queries */}
                <Card className="shadow-lg">
                    <CardHeader>
                        <CardTitle className="text-lg">Try These Sample Queries</CardTitle>
                        <p className="text-sm text-slate-600">Click any sample to use it</p>
                    </CardHeader>
                    <CardContent>
                        <div className="grid grid-cols-1 gap-3">
                            {sampleQueries.map((query, index) => (
                                <div
                                    key={index}
                                    className="group relative p-3 bg-slate-50 hover:bg-slate-100 rounded-lg border border-slate-200 hover:border-slate-300 transition-all cursor-pointer"
                                    onClick={() => handleSampleClick(query)}
                                >
                                    <p className="text-sm text-slate-700 pr-8 whitespace-pre-wrap">{query}</p>
                                    <Button
                                        variant="ghost"
                                        size="sm"
                                        className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity h-6 w-6 p-0"
                                        onClick={(e) => {
                                            e.stopPropagation()
                                            copyToClipboard(query)
                                        }}
                                    >
                                        <Copy className="h-3 w-3" />
                                    </Button>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
                {/* Results */}
                {prediction && (
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <Card className="shadow-lg">
                            <CardHeader>
                                <CardTitle className="text-center">Category Prediction</CardTitle>
                                <p className="text-center text-sm text-slate-600">
                                    Predicted:{" "}
                                    <span className="font-semibold text-slate-900">{prediction?.category}</span>
                                </p>
                            </CardHeader>
                            <CardContent>
                                <AnimatedPieChart
                                    data={categoryData}
                                    predictedValue={prediction.category}
                                    title="Category"
                                />
                            </CardContent>
                        </Card>
                        <Card className="shadow-lg">
                            <CardHeader>
                                <CardTitle className="text-center">Priority Prediction</CardTitle>
                                <p className="text-center text-sm text-slate-600">
                                    Predicted:{" "}
                                    <span className="font-semibold text-slate-900">{prediction?.priority}</span>
                                </p>
                            </CardHeader>
                            <CardContent>
                                <AnimatedPieChart
                                    data={priorityData}
                                    predictedValue={prediction.priority}
                                    title="Priority"
                                />
                            </CardContent>
                        </Card>
                    </div>
                )}
                {!prediction && !isLoading && (
                    <div className="text-center py-12">
                        <p className="text-slate-500">Enter some text above to see predictions</p>
                    </div>
                )}
            </div>
        </div>
    )
}
