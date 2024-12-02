"use client";
import { useState } from "react";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import Header from "./header";
import { Link } from "lucide-react";
import usePortfolios from "./postgres";


// Dynamic table component
export default function TableDemo() {
  const [user, setUser] = useState(null);
  const portfolios = [
    {
      name: "Portfolio A",
      dateCreated: "15 March at 10:00 AM",
      totalInvestment: "$1,000,000",
      currentValue: "$1,300,000",
      performance: "30%",
    },
    {
      name: "Portfolio B",
      dateCreated: "8 March at 08:00 AM",
      totalInvestment: "$800,000",
      currentValue: "$1,000,000",
      performance: "25%",
    },
    {
      name: "Portfolio C",
      dateCreated: "3 March at 08:00 AM",
      totalInvestment: "$1,200,000",
      currentValue: "$1,500,000",
      performance: "40%",
    },
    {
      name: "Portfolio D",
      dateCreated: "26 February at 10:00 AM",
      totalInvestment: "$500,000",
      currentValue: "$600,000",
      performance: "20%",
    },
  ];

  // Columns definition (dynamic)
  const columns = [
    { key: "name", label: "Name" },
    { key: "dateCreated", label: "Date Created" },
    { key: "totalInvestment", label: "Total Investment" },
    { key: "currentValue", label: "Current Value" },
    { key: "performance", label: "Performance" },
  ];

  return (
    <>
      <Header user={user} setUser={setUser} />
      {user ? (
        <div>
        <div className="p-7 m-7">
        <Table>
          <TableCaption>Portfolios</TableCaption>
          <TableHeader>
            <TableRow>
              {columns.map((column) => (
                <TableHead key={column.key}>{column.label}</TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody>
            {portfolios.map((portfolio, index) => (
              <TableRow key={index}>
                {columns.map((column) => (
                  <TableCell key={column.key}>
                    {portfolio[column.key]}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
          <TableFooter>
            <TableRow>
              <TableCell colSpan={columns.length}>
                {/* Add footer content here if needed */}
              </TableCell>
            </TableRow>
          </TableFooter>
        </Table>
        </div>
      
        </div>
      ) : (
        <p style={{ textAlign: "center", marginTop: "20px" }}>
          Please authenticate again to view your portfolios.
        </p>
      )}
  </>
  );
}
