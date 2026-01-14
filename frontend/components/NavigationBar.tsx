'use client';

interface NavigationBarProps {
  onMenuClick: () => void;
  modelName?: string;
}

export default function NavigationBar({ onMenuClick, modelName = 'GPT-4o' }: NavigationBarProps) {
  return (
    <nav className="fixed top-0 left-0 right-0 h-[60px] bg-white border-b border-gray-200 z-50">
      <div className="max-w-[768px] mx-auto h-full px-4 flex items-center justify-between">
        {/* Left: Hamburger Menu */}
        <button
          onClick={onMenuClick}
          className="p-2 rounded-lg hover:bg-gray-100 transition-colors"
          aria-label="Open menu"
        >
          <svg className="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>

        {/* Center: Model Badge */}
        <div className="px-3 py-1.5 bg-gray-100 rounded-full">
          <span className="text-sm font-medium text-gray-700">{modelName}</span>
        </div>

        {/* Right: Settings & Profile */}
        <div className="flex items-center gap-2">
          <button
            className="p-2 rounded-lg hover:bg-gray-100 transition-colors"
            aria-label="Settings"
          >
            <svg className="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </button>
          <button
            className="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center hover:bg-gray-400 transition-colors"
            aria-label="User profile"
          >
            <span className="text-sm font-medium text-gray-700">U</span>
          </button>
        </div>
      </div>
    </nav>
  );
}
