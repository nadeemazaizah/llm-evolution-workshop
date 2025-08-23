"""
Part 5: Advanced Multi-Agent with MCP Integration
================================================

This module demonstrates enterprise-grade agent systems using Model Context Protocol (MCP)
for dynamic external system integration and scalable architecture.
"""

import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()


class MCPTravelServer:
    """
    Mock MCP (Model Context Protocol) Server for Travel Data.

    In production, this would connect to real MCP servers providing:
    - Dynamic travel databases
    - Real-time pricing APIs
    - Content management systems
    - Enterprise travel systems
    """

    def __init__(self, server_name: str):
        self.server_name = server_name
        self.capabilities = self._get_server_capabilities()

    def _get_server_capabilities(self) -> Dict[str, Any]:
        """Get available capabilities from this MCP server."""

        capabilities_map = {
            "travel-data": {
                "resources": [
                    "destinations",
                    "attractions",
                    "restaurants",
                    "cultural_sites",
                ],
                "tools": [
                    "search_destinations",
                    "get_destination_details",
                    "find_attractions",
                ],
                "description": "Comprehensive travel destination database",
            },
            "pricing-api": {
                "resources": ["flight_prices", "hotel_rates", "activity_costs"],
                "tools": ["get_live_prices", "compare_rates", "price_alerts"],
                "description": "Real-time travel pricing and booking system",
            },
            "content-cms": {
                "resources": ["travel_guides", "local_tips", "seasonal_content"],
                "tools": ["get_content", "search_guides", "update_recommendations"],
                "description": "Dynamic travel content management system",
            },
            "enterprise-travel": {
                "resources": [
                    "corporate_rates",
                    "travel_policies",
                    "approval_workflows",
                ],
                "tools": ["check_policy", "get_corporate_rates", "submit_booking"],
                "description": "Enterprise travel management platform",
            },
        }

        return capabilities_map.get(self.server_name, {})

    def call_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Call a tool on this MCP server."""

        if self.server_name == "travel-data":
            return self._handle_travel_data_tools(tool_name, parameters)
        elif self.server_name == "pricing-api":
            return self._handle_pricing_tools(tool_name, parameters)
        elif self.server_name == "content-cms":
            return self._handle_content_tools(tool_name, parameters)
        elif self.server_name == "enterprise-travel":
            return self._handle_enterprise_tools(tool_name, parameters)

        return {"error": f"Unknown tool: {tool_name}"}

    def _handle_travel_data_tools(self, tool_name: str, params: Dict) -> Dict[str, Any]:
        """Handle travel data server tools."""

        if tool_name == "search_destinations":
            # Mock comprehensive destination search
            return {
                "destinations": [
                    {
                        "id": "barcelona_spain",
                        "name": "Barcelona, Spain",
                        "category": "Cultural/Beach",
                        "best_months": ["May", "June", "September", "October"],
                        "highlights": [
                            "Sagrada Familia",
                            "Park Güell",
                            "Gothic Quarter",
                            "La Rambla",
                        ],
                        "cuisine_specialties": [
                            "Paella",
                            "Tapas",
                            "Cava",
                            "Jamón Ibérico",
                        ],
                        "local_experiences": [
                            "Flamenco shows",
                            "Market tours",
                            "Architecture walks",
                        ],
                        "accessibility": "Excellent public transport",
                        "safety_rating": 8.5,
                        "tourist_density": "High in summer, moderate off-season",
                    }
                ],
                "total_results": 15,
                "search_metadata": {
                    "query": params.get("query", ""),
                    "filters_applied": params.get("filters", {}),
                    "timestamp": datetime.now().isoformat(),
                },
            }

        elif tool_name == "get_destination_details":
            # Mock detailed destination information
            return {
                "destination": {
                    "name": params.get("destination", "Barcelona"),
                    "detailed_info": {
                        "demographics": "Population: 1.6M, International: Very high",
                        "climate": "Mediterranean - mild winters, warm summers",
                        "transportation": {
                            "airport": "El Prat (BCN) - 12km from center",
                            "public_transport": "Metro, bus, tram - €11.20 day pass",
                            "bike_sharing": "Bicing system - tourist passes available",
                            "walking": "Highly walkable city center",
                        },
                        "districts": [
                            {
                                "name": "Ciutat Vella",
                                "description": "Historic center, Gothic Quarter",
                            },
                            {
                                "name": "Eixample",
                                "description": "Modernist architecture, shopping",
                            },
                            {
                                "name": "Gràcia",
                                "description": "Bohemian, local atmosphere",
                            },
                            {
                                "name": "Barceloneta",
                                "description": "Beach district, seafood",
                            },
                        ],
                        "cultural_calendar": {
                            "spring": "Sant Jordi Festival (April 23), Music festivals",
                            "summer": "Beach season, outdoor concerts",
                            "fall": "La Mercè Festival (September), harvest season",
                            "winter": "Christmas markets, museum season",
                        },
                    },
                }
            }

        return {"error": f"Unknown travel data tool: {tool_name}"}

    def _handle_pricing_tools(self, tool_name: str, params: Dict) -> Dict[str, Any]:
        """Handle pricing API tools."""

        if tool_name == "get_live_prices":
            return {
                "pricing_data": {
                    "flights": [
                        {
                            "route": "NYC-BCN",
                            "price": 899,
                            "airline": "Vueling",
                            "last_updated": "2024-01-10T10:30:00Z",
                        },
                        {
                            "route": "NYC-BCN",
                            "price": 1299,
                            "airline": "Lufthansa",
                            "last_updated": "2024-01-10T10:30:00Z",
                        },
                    ],
                    "hotels": [
                        {
                            "name": "Hotel Barcelona Center",
                            "price": 180,
                            "rating": 4.2,
                            "last_updated": "2024-01-10T11:00:00Z",
                        },
                        {
                            "name": "Boutique Gothic Quarter",
                            "price": 220,
                            "rating": 4.6,
                            "last_updated": "2024-01-10T11:00:00Z",
                        },
                    ],
                    "activities": [
                        {
                            "name": "Sagrada Familia Tour",
                            "price": 35,
                            "provider": "GetYourGuide",
                        },
                        {
                            "name": "Park Güell Skip-the-Line",
                            "price": 25,
                            "provider": "Viator",
                        },
                    ],
                },
                "price_trends": {
                    "flights": "Prices 15% higher than last month",
                    "hotels": "Rates stable, slight increase expected next month",
                    "activities": "Summer season pricing in effect",
                },
            }

        elif tool_name == "compare_rates":
            return {
                "comparison": {
                    "best_value_flight": {
                        "airline": "Vueling",
                        "price": 899,
                        "value_score": 9.2,
                    },
                    "best_value_hotel": {
                        "name": "Hotel Barcelona Center",
                        "price": 180,
                        "value_score": 8.8,
                    },
                    "savings_opportunities": [
                        "Book flights 6 weeks in advance for 20% savings",
                        "Weekend hotel rates 30% lower than weekdays",
                        "Activity bundles save up to €50",
                    ],
                }
            }

        return {"error": f"Unknown pricing tool: {tool_name}"}

    def _handle_content_tools(self, tool_name: str, params: Dict) -> Dict[str, Any]:
        """Handle content management tools."""

        if tool_name == "get_content":
            return {
                "content": {
                    "travel_guides": [
                        {
                            "title": "Barcelona Architecture Guide",
                            "content": "Comprehensive guide to Gaudí and modernist architecture...",
                            "last_updated": "2024-01-05",
                            "author": "Local Expert Maria Rodriguez",
                        }
                    ],
                    "local_tips": [
                        "Avoid tourist restaurants on La Rambla - go to side streets",
                        "Metro runs until 12am weekdays, 2am weekends",
                        "Many museums free first Sunday of month",
                    ],
                    "seasonal_content": {
                        "current_season": "Winter",
                        "recommendations": "Perfect museum weather, fewer crowds, lower prices",
                    },
                }
            }

        return {"error": f"Unknown content tool: {tool_name}"}

    def _handle_enterprise_tools(self, tool_name: str, params: Dict) -> Dict[str, Any]:
        """Handle enterprise travel tools."""

        if tool_name == "check_policy":
            return {
                "policy_compliance": {
                    "flight_class": "Economy approved up to $1200 for international",
                    "hotel_rate": "Max $250/night for European cities",
                    "meal_allowance": "$75/day",
                    "approval_required": False,
                    "preferred_vendors": ["Delta", "Lufthansa", "Hilton", "Marriott"],
                }
            }

        return {"error": f"Unknown enterprise tool: {tool_name}"}


class MCPIntegratedAgent(AssistantAgent):
    """
    AutoGen Agent with MCP integration capabilities.
    """

    def __init__(self, name: str, mcp_servers: List[MCPTravelServer], **kwargs):
        super().__init__(name=name, **kwargs)
        self.mcp_servers = {server.server_name: server for server in mcp_servers}

    def call_mcp_tool(
        self, server_name: str, tool_name: str, parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Call a tool on a specific MCP server."""

        if server_name in self.mcp_servers:
            return self.mcp_servers[server_name].call_tool(tool_name, parameters)
        else:
            return {"error": f"MCP server '{server_name}' not available"}

    def list_mcp_capabilities(self) -> Dict[str, Any]:
        """List all available MCP server capabilities."""

        capabilities = {}
        for server_name, server in self.mcp_servers.items():
            capabilities[server_name] = server.capabilities

        return capabilities


class AdvancedMCPTravelSystem:
    """
    Advanced multi-agent travel system with MCP integration.
    """

    def __init__(self):
        self.model_client = OpenAIChatCompletionClient(
            model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")
        )

        # Initialize MCP servers
        self.mcp_servers = [
            MCPTravelServer("travel-data"),
            MCPTravelServer("pricing-api"),
            MCPTravelServer("content-cms"),
            MCPTravelServer("enterprise-travel"),
        ]

        self.agents = self._create_mcp_integrated_agents()
        self.team = self._create_advanced_team()

    def _create_mcp_integrated_agents(self) -> Dict[str, MCPIntegratedAgent]:
        """Create MCP-integrated specialized agents."""

        agents = {}

        # Data Intelligence Agent (uses travel-data and content-cms MCP)
        agents["data_intel"] = MCPIntegratedAgent(
            name="DataIntelAgent",
            mcp_servers=[
                self.mcp_servers[0],
                self.mcp_servers[2],
            ],  # travel-data, content-cms
            model_client=self.model_client,
            system_message="""
            You are a Data Intelligence Agent with access to comprehensive travel databases via MCP.
            
            CAPABILITIES via MCP:
            - travel-data server: Detailed destination information, attractions, cultural sites
            - content-cms server: Up-to-date travel guides, local tips, seasonal content
            
            Your role:
            1. Research destinations using MCP travel-data tools
            2. Gather current local insights from content-cms
            3. Provide data-driven destination recommendations
            4. Surface hidden gems and local experiences
            5. Analyze cultural and seasonal factors
            
            Always use MCP tools to get the most current and comprehensive information.
            """,
            description="Leverages MCP servers for comprehensive travel data and content.",
        )

        # Dynamic Pricing Agent (uses pricing-api MCP)
        agents["pricing_intel"] = MCPIntegratedAgent(
            name="PricingIntelAgent",
            mcp_servers=[self.mcp_servers[1]],  # pricing-api
            model_client=self.model_client,
            system_message="""
            You are a Dynamic Pricing Intelligence Agent with real-time market access via MCP.
            
            CAPABILITIES via MCP:
            - pricing-api server: Live flight/hotel/activity prices, rate comparisons, trends
            
            Your role:
            1. Get real-time pricing data using MCP pricing tools
            2. Analyze price trends and market conditions  
            3. Identify optimal booking windows and strategies
            4. Compare rates across multiple providers
            5. Provide value optimization recommendations
            
            Always use live MCP pricing data for accurate, current market intelligence.
            """,
            description="Provides real-time pricing intelligence via MCP pricing APIs.",
        )

        # Enterprise Compliance Agent (uses enterprise-travel MCP)
        agents["compliance"] = MCPIntegratedAgent(
            name="ComplianceAgent",
            mcp_servers=[self.mcp_servers[3]],  # enterprise-travel
            model_client=self.model_client,
            system_message="""
            You are an Enterprise Travel Compliance Agent with policy system access via MCP.
            
            CAPABILITIES via MCP:
            - enterprise-travel server: Corporate policies, rates, approval workflows
            
            Your role:
            1. Check travel plans against corporate policies
            2. Access negotiated corporate rates
            3. Ensure compliance with travel guidelines
            4. Manage approval workflows when needed
            5. Optimize within enterprise constraints
            
            Always verify corporate compliance and leverage enterprise rates via MCP.
            """,
            description="Ensures enterprise travel policy compliance via MCP integration.",
        )

        # Master Orchestrator (coordinates MCP-enhanced agents)
        agents["orchestrator"] = MCPIntegratedAgent(
            name="MasterOrchestrator",
            mcp_servers=self.mcp_servers,  # Access to all MCP servers
            model_client=self.model_client,
            system_message="""
            You are the Master Orchestrator for MCP-integrated travel planning.
            
            CAPABILITIES: Access to ALL MCP servers for coordination
            - travel-data: Comprehensive destination intelligence
            - pricing-api: Real-time market pricing
            - content-cms: Current guides and local insights  
            - enterprise-travel: Corporate compliance and rates
            
            Your role:
            1. Orchestrate collaboration between specialized MCP agents
            2. Synthesize insights from multiple MCP data sources
            3. Ensure plan coherence across all systems
            4. Coordinate complex multi-system integrations
            5. Deliver enterprise-grade comprehensive plans
            
            Leverage MCP capabilities to create plans that are data-driven, 
            price-optimized, content-rich, and compliant.
            """,
            description="Orchestrates MCP-integrated agents for comprehensive planning.",
        )

        return agents

    def _create_advanced_team(self) -> RoundRobinGroupChat:
        """Create advanced team with MCP-integrated agents."""

        participants = list(self.agents.values())

        return RoundRobinGroupChat(
            participants=participants,
            max_turns=12,  # Allow for complex MCP-driven collaboration
        )

    def create_enterprise_travel_plan(
        self,
        destination: str,
        origin: str,
        departure_date: str,
        return_date: str,
        budget: float,
        traveler_profile: Dict[str, Any],
        enterprise_requirements: Dict[str, Any] = None,
    ) -> str:
        """
        Create enterprise-grade travel plan using MCP-integrated agents.
        """

        print("🔗 Initializing MCP-integrated travel planning system...")
        print(f"   🖥️  Connected MCP servers: {len(self.mcp_servers)}")
        print("   🤖 Specialized MCP agents: Data, Pricing, Compliance, Orchestrator")

        # Demonstrate MCP capabilities
        print("\n📊 MCP Server Capabilities:")
        for server in self.mcp_servers:
            print(
                f"   • {server.server_name}: {server.capabilities.get('description', 'N/A')}"
            )

        # Gather enterprise context via MCP
        print("\n🔄 Gathering enterprise intelligence via MCP...")

        enterprise_context = ""
        if enterprise_requirements:
            compliance_agent = self.agents["compliance"]
            policy_check = compliance_agent.call_mcp_tool(
                "enterprise-travel",
                "check_policy",
                {"trip_type": "international", "destination": destination},
            )
            enterprise_context = (
                f"ENTERPRISE POLICIES: {json.dumps(policy_check, indent=2)}"
            )

        # Get comprehensive data via MCP
        data_agent = self.agents["data_intel"]
        destination_data = data_agent.call_mcp_tool(
            "travel-data", "get_destination_details", {"destination": destination}
        )

        content_data = data_agent.call_mcp_tool(
            "content-cms",
            "get_content",
            {"destination": destination, "content_type": "guides_and_tips"},
        )

        # Get live pricing via MCP
        pricing_agent = self.agents["pricing_intel"]
        pricing_data = pricing_agent.call_mcp_tool(
            "pricing-api",
            "get_live_prices",
            {
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "return_date": return_date,
            },
        )

        # Create comprehensive MCP-enhanced briefing
        mcp_briefing = f"""
ENTERPRISE TRAVEL PLANNING REQUEST - MCP ENHANCED

TRIP REQUIREMENTS:
- Route: {origin} → {destination}
- Dates: {departure_date} to {return_date}
- Budget: ${budget}
- Traveler: {traveler_profile}

{enterprise_context}

MCP DATA INTELLIGENCE:

DESTINATION DATA (via travel-data MCP):
{json.dumps(destination_data, indent=2)}

CONTENT INTELLIGENCE (via content-cms MCP):
{json.dumps(content_data, indent=2)}

LIVE PRICING DATA (via pricing-api MCP):
{json.dumps(pricing_data, indent=2)}

MCP COLLABORATION INSTRUCTIONS:
- DataIntelAgent: Use travel-data and content-cms for destination intelligence
- PricingIntelAgent: Use pricing-api for market intelligence and optimization
- ComplianceAgent: Use enterprise-travel for policy compliance
- MasterOrchestrator: Synthesize all MCP data sources for comprehensive plan

Deliver an enterprise-grade plan leveraging all MCP capabilities.
"""

        print("   💬 Starting MCP-enhanced agent collaboration...")

        # Run MCP-enhanced collaboration
        result = self.team.run(
            task=mcp_briefing,
            termination_condition=lambda messages: len(messages) >= 10,
        )

        return self._format_mcp_result(result)

    def _format_mcp_result(self, result) -> str:
        """Format MCP-enhanced collaborative result."""

        messages = result.messages

        formatted_result = "=" * 100 + "\n"
        formatted_result += "🔗 MCP-INTEGRATED ENTERPRISE TRAVEL PLAN\n"
        formatted_result += "=" * 100 + "\n\n"

        # Show MCP integration benefits
        formatted_result += "🚀 MCP INTEGRATION BENEFITS:\n"
        formatted_result += "✅ Real-time data from multiple enterprise systems\n"
        formatted_result += "✅ Dynamic pricing and market intelligence\n"
        formatted_result += "✅ Corporate policy compliance automation\n"
        formatted_result += "✅ Content management system integration\n"
        formatted_result += "✅ Scalable multi-system architecture\n\n"

        # Group agent contributions
        agent_contributions = {}
        for msg in messages:
            if hasattr(msg, "source") and msg.source:
                agent_name = msg.source
                if agent_name not in agent_contributions:
                    agent_contributions[agent_name] = []
                agent_contributions[agent_name].append(msg.content)

        # Format contributions
        for agent_name, contributions in agent_contributions.items():
            formatted_result += f"\n📋 {agent_name.upper()} (MCP-Enhanced):\n"
            formatted_result += "-" * 60 + "\n"
            for contribution in contributions:
                formatted_result += f"{contribution}\n\n"

        return formatted_result


def demonstrate_mcp_integration():
    """Demonstrate MCP integration capabilities."""

    print("=" * 100)
    print("PART 5: ADVANCED MULTI-AGENT WITH MCP INTEGRATION")
    print("=" * 100)

    # Initialize MCP-integrated system
    mcp_system = AdvancedMCPTravelSystem()

    # Enterprise travel scenario
    traveler_profile = {
        "role": "Senior Executive",
        "preferences": "Efficiency, comfort, cultural experiences",
        "constraints": "Tight schedule, high-value meetings",
    }

    enterprise_requirements = {
        "policy_compliance": True,
        "corporate_rates": True,
        "approval_required": False,
        "expense_tracking": True,
    }

    print(f"\n🎯 ENTERPRISE MCP SCENARIO:")
    print(f"   Business trip: London → Tokyo")
    print(f"   Traveler: {traveler_profile['role']}")
    print(f"   Requirements: Corporate compliance, optimal pricing")
    print(f"   MCP Servers: {len(mcp_system.mcp_servers)} connected")

    # Show MCP server capabilities
    print(f"\n🖥️  MCP SERVER ECOSYSTEM:")
    for i, server in enumerate(mcp_system.mcp_servers, 1):
        caps = server.capabilities
        print(f"   {i}. {server.server_name}:")
        print(f"      • Resources: {', '.join(caps.get('resources', []))}")
        print(f"      • Tools: {', '.join(caps.get('tools', []))}")
        print(f"      • Purpose: {caps.get('description', 'N/A')}")

    print("=" * 100)

    # Run MCP-enhanced planning
    mcp_plan = mcp_system.create_enterprise_travel_plan(
        destination="Tokyo, Japan",
        origin="London, UK",
        departure_date="2024-04-15",
        return_date="2024-04-22",
        budget=5000,
        traveler_profile=traveler_profile,
        enterprise_requirements=enterprise_requirements,
    )

    print(mcp_plan)


def demonstrate_mcp_architecture():
    """Show MCP architecture and benefits."""

    print("\n" + "=" * 80)
    print("🏗️  MCP ARCHITECTURE & BENEFITS")
    print("=" * 80)

    architecture_info = """
    
🔗 MODEL CONTEXT PROTOCOL (MCP) ARCHITECTURE:

┌─────────────────────────────────────────────────────────────┐
│                    AUTOGEN AGENTS                           │
├─────────────────────────────────────────────────────────────┤
│  DataIntel │ PricingIntel │ Compliance │ Orchestrator      │
│   Agent    │    Agent     │   Agent    │    Agent          │
└─────────────────┬───────────────┬──────────────┬────────────┘
                  │               │              │
            ┌─────┴─────┐   ┌─────┴─────┐  ┌────┴────┐
            │    MCP    │   │    MCP    │  │   MCP   │
            │ Protocol  │   │ Protocol  │  │Protocol │
            └─────┬─────┘   └─────┬─────┘  └────┬────┘
                  │               │              │
        ┌─────────┴─────────┐ ┌───┴────┐ ┌─────┴──────┐
        │   travel-data     │ │pricing-│ │enterprise- │
        │     server        │ │   api  │ │   travel   │
        │                   │ │ server │ │   server   │
        └───────────────────┘ └────────┘ └────────────┘

🚀 MCP BENEFITS:

SCALABILITY:
✅ Add new data sources without code changes
✅ Dynamic capability discovery
✅ Horizontal system scaling

FLEXIBILITY:
✅ Hot-swap data providers
✅ A/B test different APIs
✅ Environment-specific configurations

MAINTAINABILITY:  
✅ Centralized data source management
✅ Standardized integration patterns
✅ Reduced coupling between agents and data

ENTERPRISE READY:
✅ Security and compliance layers
✅ Audit trails and monitoring
✅ Multi-tenant support

REAL-WORLD APPLICATIONS:
• Financial trading systems
• Healthcare data integration  
• Supply chain management
• Customer service platforms
"""
    print(architecture_info)


if __name__ == "__main__":
    # Check dependencies
    try:
        import autogen_agentchat

        print("✅ AutoGen AgentChat available")
    except ImportError:
        print("❌ AutoGen AgentChat required. Run: pip install autogen-agentchat")

    # Run demonstrations
    demonstrate_mcp_integration()
    demonstrate_mcp_architecture()

    print("\n" + "=" * 100)
    print("🎓 WORKSHOP CONCLUSION: LLM EVOLUTION JOURNEY COMPLETE")
    print("=" * 100)

    evolution_summary = """
    
🗺️  JOURNEY RECAP - From Simple to Sophisticated:

1️⃣  SIMPLE LLM PROMPTING
    → Basic responses, no context, no real-time data
    → Use case: Quick prototypes, static information
    
2️⃣  RAG ENHANCEMENT  
    → Added knowledge base, contextual responses
    → Use case: Knowledge-intensive applications
    
3️⃣  SINGLE AGENT + TOOLS
    → Real-time data, external API integration  
    → Use case: Personal assistants, dynamic workflows
    
4️⃣  MULTI-AGENT COLLABORATION
    → Specialized expertise, coordinated workflows
    → Use case: Complex domains, enterprise applications
    
5️⃣  MCP-INTEGRATED AGENTS
    → Enterprise scalability, dynamic system integration
    → Use case: Production systems, multi-tenant platforms

🎯 KEY TAKEAWAYS:

PROGRESSION LOGIC:
• Start simple, add complexity as needed
• Each level solves specific limitations
• Choose based on requirements, not trends

TECHNICAL EVOLUTION:
• Prompting → Context → Tools → Collaboration → Integration
• Single → Multiple → Coordinated → Scalable
• Static → Dynamic → Intelligent → Adaptive

BUSINESS VALUE:
• Simple: Fast prototyping
• RAG: Knowledge applications  
• Tools: Real-time systems
• Multi-agent: Enterprise complexity
• MCP: Production scalability

🚀 NEXT STEPS:
1. Experiment with each approach
2. Build increasingly complex systems
3. Consider production requirements early
4. Design for scalability and maintainability
"""

    print(evolution_summary)

    print("\n" + "=" * 100)
    print("Thank you for joining the LLM Evolution Workshop!")
    print("🌟 You've mastered the journey from simple prompts to enterprise agents!")
    print("=" * 100)
