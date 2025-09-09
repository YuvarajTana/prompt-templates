/**
 * TaskFlow AI - Root Layout
 * 
 * Following Frontend Template Epic 1: Layout & Navigation Systems
 * - Main layout structure
 * - Theme provider setup
 * - Global providers and context
 */

import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'TaskFlow AI - Intelligent Task Management',
  description: 'AI-powered task management platform that helps individuals and companies manage their tasks more effectively through smart automation, predictive insights, and workflow optimization.',
  keywords: 'task management, AI, productivity, automation, workflow',
  authors: [{ name: 'TaskFlow AI Team' }],
  robots: 'index, follow',
}

export const viewport = {
  width: 'device-width',
  initialScale: 1,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
      </body>
    </html>
  )
}
