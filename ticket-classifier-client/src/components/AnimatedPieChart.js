"use client"

import { useEffect, useState } from "react"
import { PieChart, Pie, Cell, ResponsiveContainer } from "recharts"
import { motion, AnimatePresence } from "framer-motion"

export function AnimatedPieChart({ data, predictedValue, title }) {
    const [animatedData, setAnimatedData] = useState(data.map((item) => ({ ...item, value: 0 })))
  
    useEffect(() => {
      // Animate data values
      const timer = setTimeout(() => {
        setAnimatedData(data)
      }, 300)
  
      return () => clearTimeout(timer)
    }, [data, predictedValue])
  
    const renderCustomLabel = ({ cx, cy, midAngle, innerRadius, outerRadius, name, value }) => {
      const RADIAN = Math.PI / 180
      const radius = outerRadius + 30
      const x = cx + radius * Math.cos(-midAngle * RADIAN)
      const y = cy + radius * Math.sin(-midAngle * RADIAN)
  
      return (
        <text
          x={x}
          y={y}
          fill="#374151"
          textAnchor={x > cx ? "start" : "end"}
          dominantBaseline="central"
          className={`text-sm ${name === predictedValue ? "font-bold" : "font-medium"}`}
        >
          {`${name}`}
        </text>
      )
    }
  
    const renderActiveShape = (props) => {
      const { cx, cy, midAngle, innerRadius, outerRadius, startAngle, endAngle, fill, payload } = props
  
      if (payload.name !== predictedValue) {
        return (
          <g>
            <Sector
              cx={cx}
              cy={cy}
              innerRadius={innerRadius}
              outerRadius={outerRadius}
              startAngle={startAngle}
              endAngle={endAngle}
              fill={fill}
            />
          </g>
        )
      }
  
      // Enhanced rendering for predicted slice
      return (
        <g>
          {/* Glow effect */}
          <Sector
            cx={cx}
            cy={cy}
            innerRadius={innerRadius - 2}
            outerRadius={outerRadius + 8}
            startAngle={startAngle}
            endAngle={endAngle}
            fill={fill}
            opacity={0.3}
            filter="blur(4px)"
          />
          {/* Main slice - pulled out */}
          <Sector
            cx={cx}
            cy={cy}
            innerRadius={innerRadius}
            outerRadius={outerRadius + 5}
            startAngle={startAngle}
            endAngle={endAngle}
            fill={fill}
            stroke="#1f2937"
            strokeWidth={3}
          />
        </g>
      )
    }
  
    // Custom Sector component since Recharts doesn't export it
    const Sector = ({ cx, cy, innerRadius, outerRadius, startAngle, endAngle, fill, ...props }) => {
      const RADIAN = Math.PI / 180
      const sin = Math.sin(-RADIAN * endAngle)
      const cos = Math.cos(-RADIAN * endAngle)
      const mx = cx + ((outerRadius + innerRadius) / 2) * cos
      const my = cy + ((outerRadius + innerRadius) / 2) * sin
      const ex = mx + (cos >= 0 ? 1 : -1) * 22
      const ey = my
      const textAnchor = cos >= 0 ? "start" : "end"
  
      return (
        <g>
          <path
            d={`M ${cx},${cy} L ${cx + innerRadius * Math.cos(-RADIAN * startAngle)},${cy + innerRadius * Math.sin(-RADIAN * startAngle)} A ${innerRadius},${innerRadius} 0 ${endAngle - startAngle > 180 ? 1 : 0},0 ${cx + innerRadius * Math.cos(-RADIAN * endAngle)},${cy + innerRadius * Math.sin(-RADIAN * endAngle)} L ${cx + outerRadius * Math.cos(-RADIAN * endAngle)},${cy + outerRadius * Math.sin(-RADIAN * endAngle)} A ${outerRadius},${outerRadius} 0 ${endAngle - startAngle > 180 ? 1 : 0},1 ${cx + outerRadius * Math.cos(-RADIAN * startAngle)},${cy + outerRadius * Math.sin(-RADIAN * startAngle)} Z`}
            fill={fill}
            {...props}
          />
        </g>
      )
    }
  
    return (
      <div className="relative w-full h-80">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={animatedData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={renderCustomLabel}
              outerRadius={80}
              innerRadius={30}
              fill="#8884d8"
              dataKey="value"
              animationBegin={0}
              animationDuration={1000}
            >
              {animatedData.map((entry, index) => {
                const isPredicted = entry.name === predictedValue
                return (
                  <Cell
                    key={`cell-${index}`}
                    fill={entry.color}
                    stroke={isPredicted ? "#1f2937" : "transparent"}
                    strokeWidth={isPredicted ? 3 : 0}
                    style={{
                      filter: isPredicted ? "drop-shadow(0 4px 8px rgba(0,0,0,0.3))" : "none",
                      transform: isPredicted ? "scale(1.05)" : "scale(1)",
                      transformOrigin: "center",
                    }}
                  />
                )
              })}
            </Pie>
          </PieChart>
        </ResponsiveContainer>
  
        {/* Center Hub with pulsing effect */}
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <motion.div
            className="w-8 h-8 bg-slate-800 rounded-full shadow-lg border-2 border-white flex items-center justify-center"
            animate={{
              scale: [1, 1.1, 1],
              boxShadow: ["0 4px 8px rgba(0,0,0,0.3)", "0 8px 16px rgba(0,0,0,0.4)", "0 4px 8px rgba(0,0,0,0.3)"],
            }}
            transition={{
              duration: 2,
              repeat: Number.POSITIVE_INFINITY,
              ease: "easeInOut",
            }}
          >
            <div className="w-2 h-2 bg-white rounded-full" />
          </motion.div>
        </div>
  
        {/* Prediction Badge with enhanced styling */}
        <motion.div
          className="absolute bottom-0 left-1/2 transform -translate-x-1/2"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1, duration: 0.5 }}
        >
          <motion.div
            className="bg-gradient-to-r from-slate-800 to-slate-700 text-white px-3 py-1 rounded-full text-sm font-semibold shadow-lg border border-slate-600"
            animate={{
              boxShadow: ["0 4px 8px rgba(0,0,0,0.3)", "0 6px 12px rgba(0,0,0,0.4)", "0 4px 8px rgba(0,0,0,0.3)"],
            }}
            transition={{
              duration: 2,
              repeat: Number.POSITIVE_INFINITY,
              ease: "easeInOut",
            }}
          >
            {predictedValue}
          </motion.div>
        </motion.div>
      </div>
    )
  }
