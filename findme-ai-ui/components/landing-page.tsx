'use client'

import { useState, useRef } from "react"
import { Button } from "@/components/ui/button"
import { ArrowRight, BookOpen, Users, Zap, Compass, FileQuestion } from "lucide-react"

export function LandingPage() {
  const [showQuestionnaire, setShowQuestionnaire] = useState(false)
  const questionnaireRef = useRef<HTMLDivElement>(null)

  const scrollToQuestionnaire = () => {
    setShowQuestionnaire(true)
    setTimeout(() => {
      questionnaireRef.current?.scrollIntoView({ behavior: 'smooth' })
    }, 100)
  }

  return (
    <div className="flex flex-col min-h-screen">
      <header className="w-full border-b">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
          <a className="flex items-center justify-center" href="#">
            <Compass className="h-6 w-6 text-primary" />
            <span className="ml-2 text-lg font-bold">FindMe AI</span>
          </a>
          <nav className="flex gap-4 sm:gap-6">
            <a className="text-sm font-medium hover:underline underline-offset-4" href="#">
              Features
            </a>
            <a className="text-sm font-medium hover:underline underline-offset-4" href="#">
              How It Works
            </a>
            <button
              className="text-sm font-medium hover:underline underline-offset-4"
              onClick={scrollToQuestionnaire}
            >
              Questionnaire
            </button>
            <a className="text-sm font-medium hover:underline underline-offset-4" href="#">
              About
            </a>
            <a className="text-sm font-medium hover:underline underline-offset-4" href="#">
              Contact
            </a>
          </nav>
        </div>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-gradient-to-b from-primary-50 to-white dark:from-gray-900 dark:to-gray-800">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                  Discover Your Perfect Learning Path with FindMe AI
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  Unlock a personalized journey to growth. Connect with tailored opportunities that align with your interests and goals.
                </p>
              </div>
              <div className="w-full max-w-sm space-y-2">
                <Button className="w-full" size="lg" onClick={scrollToQuestionnaire}>
                  Start Questionnaire
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                  Begin your personalized learning adventure today. No credit card required.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-white dark:bg-gray-900">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl text-center mb-12">How FindMe AI Works</h2>
            <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
              <div className="flex flex-col items-center space-y-4">
                <div className="bg-primary/10 p-3 rounded-full">
                  <FileQuestion className="h-10 w-10 text-primary" />
                </div>
                <h3 className="text-xl font-bold">Smart Questionnaire</h3>
                <p className="text-center text-gray-500 dark:text-gray-400">
                  Our adaptive questionnaire understands your unique interests, learning goals, and ambitions.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4">
                <div className="bg-primary/10 p-3 rounded-full">
                  <Compass className="h-10 w-10 text-primary" />
                </div>
                <h3 className="text-xl font-bold">Personalized Pathway</h3>
                <p className="text-center text-gray-500 dark:text-gray-400">
                  Get a customized learning roadmap with events, courses, and clubs tailored to your journey.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4">
                <div className="bg-primary/10 p-3 rounded-full">
                  <Users className="h-10 w-10 text-primary" />
                </div>
                <h3 className="text-xl font-bold">Community Connection</h3>
                <p className="text-center text-gray-500 dark:text-gray-400">
                  Discover and connect with like-minded individuals in your university and local community.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col items-center space-y-4 text-center">
              <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Your Learning Journey Awaits</h2>
              <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                With FindMe AI, you're just steps away from unlocking a world of personalized learning opportunities. Our smart questionnaire is the key to crafting your unique educational path.
              </p>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-white dark:bg-gray-900">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid gap-10 lg:grid-cols-2">
              <div className="flex flex-col justify-center space-y-4">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Why Choose FindMe AI?</h2>
                <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  FindMe AI simplifies your learning journey by connecting you with the right opportunities. Our app filters through countless options to find those that match your specific learning interests and goals.
                </p>
                <ul className="grid gap-6 mt-6">
                  <li className="flex items-center">
                    <BookOpen className="mr-2 h-4 w-4 text-primary" />
                    <span>Access to a wide range of learning opportunities</span>
                  </li>
                  <li className="flex items-center">
                    <Users className="mr-2 h-4 w-4 text-primary" />
                    <span>Connect with like-minded individuals</span>
                  </li>
                  <li className="flex items-center">
                    <Compass className="mr-2 h-4 w-4 text-primary" />
                    <span>Track your progress and stay motivated</span>
                  </li>
                </ul>
              </div>
              <div className="flex items-center justify-center">
                <div className="relative w-full max-w-sm">
                  <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-primary to-primary-foreground opacity-50 rounded-lg blur-xl"></div>
                  <div className="relative bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 p-8 rounded-lg shadow-2xl">
                    <BookOpen className="h-12 w-12 text-primary mb-4" />
                    <h3 className="text-2xl font-bold mb-2">Start Learning Today</h3>
                    <p className="text-gray-500 dark:text-gray-400 mb-4">Join thousands of learners who have found their perfect path with FindMe AI.</p>
                    <Button className="w-full" onClick={scrollToQuestionnaire}>
                      Take the Questionnaire
                      <ArrowRight className="ml-2 h-4 w-4" />
                    </Button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        {showQuestionnaire && (
          <section ref={questionnaireRef} className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8">
              <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl text-center mb-8">FindMe AI Questionnaire</h2>
              <div className="w-full max-w-4xl mx-auto aspect-video">
                <iframe
                  src="https://your-streamlit-app-url.com"
                  title="FindMe AI Questionnaire"
                  className="w-full h-full border-0 rounded-lg shadow-lg"
                />
              </div>
            </div>
          </section>
        )}
      </main>
      <footer className="w-full border-t">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-6 flex flex-col sm:flex-row justify-between items-center">
          <p className="text-xs text-gray-500 dark:text-gray-400">© 2024 FindMe AI. All rights reserved.</p>
          <nav className="flex gap-4 sm:gap-6 mt-4 sm:mt-0">
            <a className="text-xs hover:underline underline-offset-4" href="#">
              Terms of Service
            </a>
            <a className="text-xs hover:underline underline-offset-4" href="#">
              Privacy Policy
            </a>
          </nav>
        </div>
      </footer>
    </div>
  )
}