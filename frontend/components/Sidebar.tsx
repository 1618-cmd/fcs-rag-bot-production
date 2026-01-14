'use client';

import { useState, useEffect } from 'react';

interface Conversation {
  id: string;
  title: string;
  timestamp: Date;
  messageCount: number;
}

interface SidebarProps {
  conversations: Conversation[];
  currentConversationId: string | null;
  onNewChat: () => void;
  onSelectConversation: (id: string) => void;
  onDeleteConversation: (id: string) => void;
  isOpen: boolean;
  onToggle: () => void;
}

interface GroupedConversations {
  today: Conversation[];
  yesterday: Conversation[];
  week: Conversation[];
  month: Conversation[];
  older: Conversation[];
}

export default function Sidebar({
  conversations,
  currentConversationId,
  onNewChat,
  onSelectConversation,
  onDeleteConversation,
  isOpen,
  onToggle,
}: SidebarProps) {
  const [grouped, setGrouped] = useState<GroupedConversations>({
    today: [],
    yesterday: [],
    week: [],
    month: [],
    older: [],
  });

  useEffect(() => {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const yesterday = new Date(today);
    yesterday.setDate(yesterday.getDate() - 1);
    const weekAgo = new Date(today);
    weekAgo.setDate(weekAgo.getDate() - 7);
    const monthAgo = new Date(today);
    monthAgo.setDate(monthAgo.getDate() - 30);

    const grouped: GroupedConversations = {
      today: [],
      yesterday: [],
      week: [],
      month: [],
      older: [],
    };

    conversations.forEach((conv) => {
      const convDate = new Date(conv.timestamp);
      if (convDate >= today) {
        grouped.today.push(conv);
      } else if (convDate >= yesterday) {
        grouped.yesterday.push(conv);
      } else if (convDate >= weekAgo) {
        grouped.week.push(conv);
      } else if (convDate >= monthAgo) {
        grouped.month.push(conv);
      } else {
        grouped.older.push(conv);
      }
    });

    setGrouped(grouped);
  }, [conversations]);

  const formatTime = (date: Date) => {
    const now = new Date();
    const diff = now.getTime() - new Date(date).getTime();
    const minutes = Math.floor(diff / 60000);
    const hours = Math.floor(diff / 3600000);

    if (minutes < 1) return 'Just now';
    if (minutes < 60) return `${minutes}m ago`;
    if (hours < 24) return `${hours}h ago`;
    return new Date(date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  const renderGroup = (title: string, convs: Conversation[]) => {
    if (convs.length === 0) return null;

    return (
      <div className="mb-6">
        <h3 className="px-4 py-2 text-xs font-semibold text-[#6B7280] uppercase tracking-wide">
          {title}
        </h3>
        <div className="space-y-1">
          {convs.map((conv) => (
            <div
              key={conv.id}
              className="group relative px-4 py-2.5 hover:bg-gray-100 rounded-lg mx-2 cursor-pointer transition-colors"
              onClick={() => {
                onSelectConversation(conv.id);
                onToggle();
              }}
            >
              <div className="flex items-start justify-between">
                <div className="flex-1 min-w-0">
                  <p
                    className={`text-sm truncate ${
                      currentConversationId === conv.id
                        ? 'font-medium text-[#1F2937]'
                        : 'text-[#6B7280]'
                    }`}
                  >
                    {conv.title}
                  </p>
                  <p className="text-xs text-[#6B7280] mt-0.5">{formatTime(conv.timestamp)}</p>
                </div>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    onDeleteConversation(conv.id);
                  }}
                  className="opacity-0 group-hover:opacity-100 p-1 rounded hover:bg-gray-200 transition-opacity ml-2"
                  aria-label="Delete conversation"
                >
                  <svg className="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <>
      {/* Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 lg:hidden transition-opacity"
          onClick={onToggle}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`
          fixed lg:relative
          inset-y-0 left-0
          z-50
          w-[280px] flex-shrink-0
          bg-white border-r border-gray-200
          flex flex-col
          h-screen
          transform transition-transform duration-250 ease-out
          ${isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'}
          shadow-lg lg:shadow-none
        `}
      >
        {/* Header */}
        <div className="p-4 border-b border-gray-200">
          <button
            onClick={onNewChat}
            className="w-full px-4 py-2.5 bg-[#D97757] text-white rounded-lg font-medium hover:bg-[#C4694A] transition-colors"
          >
            New Chat
          </button>
        </div>

        {/* Conversation List */}
        <div className="flex-1 overflow-y-auto py-4">
          {conversations.length === 0 ? (
            <div className="px-4 py-8 text-center">
              <p className="text-sm text-[#6B7280]">No conversations yet</p>
              <p className="text-xs text-[#6B7280] mt-1">Start a new chat to begin</p>
            </div>
          ) : (
            <>
              {renderGroup('Today', grouped.today)}
              {renderGroup('Yesterday', grouped.yesterday)}
              {renderGroup('Previous 7 Days', grouped.week)}
              {renderGroup('Previous 30 Days', grouped.month)}
              {renderGroup('Older', grouped.older)}
            </>
          )}
        </div>
      </aside>
    </>
  );
}
