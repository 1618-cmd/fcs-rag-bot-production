/**
 * Container Component
 * 
 * Reusable container for consistent width constraints across the app
 */

interface ContainerProps {
  children: React.ReactNode;
  size?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  className?: string;
}

export default function Container({ 
  children, 
  size = 'md',
  className = '' 
}: ContainerProps) {
  
  const sizeMap = {
    sm: '576px',   // Narrow
    md: '672px',   // ChatGPT text width
    lg: '768px',   // Medium
    xl: '896px',   // Wide
    full: '100%'   // Full width
  };

  return (
    <div 
      style={{ 
        maxWidth: sizeMap[size], 
        margin: '0 auto', 
        padding: '0 24px',
        width: '100%',
        boxSizing: 'border-box'
      }}
      className={`${className} overflow-x-hidden`}
    >
      {children}
    </div>
  );
}
